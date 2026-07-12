with open(r"c:\Users\DE PAULA\Desktop\Ecotenébrios\web\css\style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "pet-segment-card" in line or "pet-icon" in line:
        print(f"Line {i+1}: {line.strip()}")
