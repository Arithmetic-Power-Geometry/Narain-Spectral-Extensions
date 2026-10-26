#!/usr/bin/env python3
"""P01 reproducible metadata and theorem-scope lint; no numerical proof claims."""
from pathlib import Path
import csv, re, json
root=Path(__file__).resolve().parents[2]
bib=(root/"reference/references.bib").read_text()
rows=list(csv.DictReader((root/"reference/verification_register.tsv").open(),delimiter="\t"))
keys=re.findall(r"@article\{([^,]+),",bib)
assert len(keys)==len(set(keys)), "duplicate BibTeX keys"
assert len(rows)==len(keys), "verification register / BibTeX count mismatch"
assert set(keys)=={r["key"] for r in rows}, "missing verification records"
for r in rows:
 assert r["status"]=="VERIFIED" and r["primary_source_url"].startswith("https://"),r
assert "3373/1325" in (root/"evidence/P01/audit.md").read_text()
assert "3313/1325" in (root/"evidence/P01/audit.md").read_text()
print(json.dumps({"status":"PASS","checked_bib_records":len(keys),"verified_keys":keys,"scope":"metadata register and audit text only"},indent=2))
