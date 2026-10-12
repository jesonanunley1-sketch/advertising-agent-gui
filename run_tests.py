import json
from pathlib import Path
from agent import process_instruction
cases=json.loads((Path(__file__).parent/"test_cases.json").read_text(encoding="utf-8"))
failed=0
for c in cases:
    actual=process_instruction(c["input"])
    ok=actual==c["expected"]
    print(("PASS" if ok else "FAIL")+" "+c["id"])
    if not ok:
        print(" expected:",c["expected"]); print(" actual:",actual); failed+=1
raise SystemExit(1 if failed else 0)
