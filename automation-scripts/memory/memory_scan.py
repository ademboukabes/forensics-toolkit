import subprocess, sys, os

if len(sys.argv) < 2:
    print("Usage: python memory_scan.py <memory_image>")
    sys.exit(1)

mem = sys.argv[1]
out = "reports/memory"
os.makedirs(out, exist_ok=True)

plugins = ["pslist","netscan","cmdline"]

print(f"Analyzing memory image: {mem}")

for p in plugins:
    print(f"Running plugin: {p}...")
    # Assumes 'vol' matches the volatility3 command on the system
    subprocess.run(
        f"vol -f {mem} windows.{p} > {out}/{p}.txt",
        shell=True
    )

print(f"Analysis complete. Reports saved in {out}/")
