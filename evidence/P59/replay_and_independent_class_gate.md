# P59: P58 byte-identical replay and independent LC-class audit

Date: 2026-10-27.

## P58 replay, closed reproducibility gap
Reconstructed evidence/P58/exhaustive_n6.py from the local original by removing only unused helper/comment lines, then compared the reconstructed file Git blob to the independently fetched GitHub blob: BOTH 9d8a83b004b48be2d04af4c5dd807f8a3a649115. This establishes byte identity for the replayed committed source, not merely functional similarity. Replayed /mnt/data/p58/replay_committed.py under 35-second timeout: exit 0, wall 7.37s, RSS 98576 KB. Output: 32768 labeled graphs, 64 signatures, 26 LC/permutation classes, zero cross-class shared-signature groups, zero cross-class graph pairs. Source SHA256 323b0ae397dde343ea83a0213c1eccaf9109d2046415ba7b2f7e54b2bdc758b8; stdout SHA256 1f55170dd7a3d0ae9815da107473bbb3b68f2fa862782d2746d103aa1e61d9f9; stderr empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources SHA256 0f877718bc733cf9c66d15941178b8a51c439dd28eece5352a9a8896e3e9b9e0.

## Independent equivalence-class cross-check
Using NetworkX 3.6.1 graph_atlas_g (156 unlabeled six-vertex graphs), an independent algorithm applied local complementation, identified resulting unlabeled graphs using nx.is_isomorphic, and breadth-first enumerated LC classes. It found exactly 26 classes, independently corroborating P58's class count. Sizes of these classes in unlabeled graph representatives: [1,1,1,1,2,2,2,2,2,2,2,3,3,4,4,4,5,5,6,6,10,10,16,16,21,25]. This does NOT independently verify the 64 coarse signatures or absence of cross-class collisions; those are supported by the byte-identical P58 replay.

Independent executable source: evidence/P59/independent_atlas_check.py, executed local /mnt/data/p58/atlas_independent.py, Git blob f51c3a549162c7a1addcb087a2f6865ef2ba889a byte-identical; SHA256 source 3b580a289138f3fba4dd1c42ef7eab5728a9ca2882b8ccef0aebfc0429741bfe; stdout 9ace1fa609b31ff6a91add0aa085087aa33cf7cc5400651c6807382ed56d8e08; stderr empty e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources f4a76b8820999c1bd54b6b69504dff91ab2badbede6ba570cfa0c404ae3cbf1e. Exit 0; wall from time resource file; algorithm internal 1.669s.

## Gate
GO: P58 committed source replayed byte-identically; independent six-vertex LC class count agrees.
REVISE: independently implement coarse signature collision audit, archive raw logs remotely, pin software and verify physical CFT interpretation.
NO-GO: novel Narain physics result, general theorem, original Q1 submission.
Next bounded step: independent signature-to-LC-class audit using NetworkX atlas or a separate codeword enumerator; no n7 expansion without novelty hypothesis.
