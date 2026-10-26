#!/usr/bin/env python3
"""P18 original-source runner. Execute at a pinned Git checkout; never edits originals."""
import sys,os,json,hashlib,subprocess,platform,time,pathlib,difflib
root=pathlib.Path(__file__).resolve().parents[2]
out=root/'evidence/P18/ci_run'
out.mkdir(parents=True,exist_ok=True)
paths=['evidence/P01/check_metadata.py','evidence/P02/independent_checker.py']+[f'evidence/P{i:02d}/check.py' for i in range(3,10)]
commit=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True)
matrix={'git_commit':commit.stdout.strip() if commit.returncode==0 else None,'python':sys.version,'platform':platform.platform(),'runs':[]}
def diff(a,b,path='$'):
 if type(a)!=type(b):return [{'path':path,'kind':'type','expected_type':type(b).__name__,'actual_type':type(a).__name__}]
 if isinstance(a,dict):
  rows=[]
  for k in sorted(a.keys()|b.keys()):
   if k not in a:rows.append({'path':path+'.'+k,'kind':'missing_actual'})
   elif k not in b:rows.append({'path':path+'.'+k,'kind':'missing_expected'})
   else:rows.extend(diff(a[k],b[k],path+'.'+k))
  return rows
 if isinstance(a,list):
  rows=[] if len(a)==len(b) else [{'path':path,'kind':'length','actual':len(a),'expected':len(b)}]
  for i in range(min(len(a),len(b))):rows.extend(diff(a[i],b[i],f'{path}[{i}]'))
  return rows
 return [] if a==b else [{'path':path,'kind':'value','actual':a,'expected':b}]
for rel in paths:
 p=root/rel;phase=p.parent.name;rec={'phase':phase,'source':rel,'exists':p.is_file()}
 if p.is_file():
  rec['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
  t=time.monotonic()
  try:
   cmd=[sys.executable,str(p)]
   run=subprocess.run(cmd,cwd=root,capture_output=True,timeout=300)
   rec.update(exit_code=run.returncode,elapsed_seconds=round(time.monotonic()-t,3),stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),stderr_sha256=hashlib.sha256(run.stderr).hexdigest())
   (out/(phase+'.stdout')).write_bytes(run.stdout);(out/(phase+'.stderr')).write_bytes(run.stderr)
   expected=p.parent/'results.json'
   try:
    actual=json.loads(run.stdout);rec['stdout_valid_json']=True
    if expected.is_file():
     baseline=json.loads(expected.read_text());differences=diff(actual,baseline);rec['json_equal']=not differences;rec['differences_count']=len(differences)
     (out/(phase+'.json_diff.json')).write_text(json.dumps(differences,indent=2,default=str)+'\n')
    else:rec['baseline_missing']=True
   except Exception as e:rec['json_error']=repr(e)
  except Exception as e:rec['execution_error']=repr(e)
 matrix['runs'].append(rec)
 (out/'matrix.json').write_text(json.dumps(matrix,indent=2)+'\n')
 print(json.dumps(rec),flush=True)
print('All outputs are observations; JSON schema differences are not automatically mathematical failures.')
