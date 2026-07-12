import json

with open(r"c:\Users\DE PAULA\Desktop\Ecotenébrios\saidas\detector_findings_final.json", "r", encoding="utf-8") as f:
    findings = json.load(f)

warnings = [f for f in findings if f.get("severity") == "warning"]
print(f"Total findings: {len(findings)}")
print(f"Total warnings: {len(warnings)}")
for w in warnings:
    print(f"- {w.get('ruleId')}: {w.get('message')} at {w.get('filePath')}:{w.get('line')}")
