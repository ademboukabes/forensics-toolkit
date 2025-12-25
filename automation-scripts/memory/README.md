# Memory Forensics Module

## script: memory_scan.py

This script automates memory dump analysis using Volatility 3.

### Features
- Process listing (`pslist`)
- Network connection scanning (`netscan`)
- Command line history (`cmdline`)

### Usage
From the project root:
```bash
python automation-scripts/memory/memory_scan.py <path_to_memory_dump>
```

### Dependencies
- Volatility 3 (`vol` command in PATH)
- Python 3
