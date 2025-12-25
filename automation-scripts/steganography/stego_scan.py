import subprocess, sys, os

if len(sys.argv) < 2:
    print("Usage: python stego_scan.py <image_file>")
    sys.exit(1)

img = sys.argv[1]
out = "reports/stego"
os.makedirs(out, exist_ok=True)

cmds = [
    f"strings {img}",
    f"exiftool {img}",
    f"binwalk {img}",
    f"steghide extract -sf {img} -p ''"
]

output_file = f"{out}/stego_report.txt"
print(f"Scanning image {img} with multiple tools...")

with open(output_file,"w") as f:
    for c in cmds:
        print(f"Running: {c}")
        f.write(f"\n[+] {c}\n")
        f.write(subprocess.getoutput(c))

print(f"Stego report generated at {output_file}")
