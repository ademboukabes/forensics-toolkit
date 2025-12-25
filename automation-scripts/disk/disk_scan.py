import os, subprocess, hashlib, sys

def run(cmd):
    return subprocess.getoutput(cmd)

def hash_file(f):
    h = hashlib.sha256()
    with open(f,'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

if len(sys.argv) < 2:
    print("Usage: python disk_scan.py <image_file>")
    sys.exit(1)

target = sys.argv[1]
# Output directory relative to where the script is executed
out = f"reports/disk_{os.path.basename(target)}"
os.makedirs(out, exist_ok=True)

with open(f"{out}/report.txt","w") as r:
    r.write(f"[+] FILE TYPE\n{run(f'file {target}')}\n\n")
    r.write(f"[+] SHA256\n{hash_file(target)}\n\n")
    r.write(f"[+] STRINGS\n{run(f'strings {target} | head')}\n\n")
    r.write(f"[+] EXIF\n{run(f'exiftool {target}')}\n\n")

print(f"Report generated at {out}/report.txt")
