# Disk Forensics Module

## script: disk_scan.py

This script automates basic disk forensics tasks.

### Features
- Data type detection (`file`)
- SHA256 Hashing
- String extraction (`strings`)
- Metadata extraction (`exiftool`)

### Usage
From the project root:
```bash
python automation-scripts/disk/disk_scan.py <path_to_image>
```

### Dependencies
- `file` command
- `strings` command
- `exiftool` command
