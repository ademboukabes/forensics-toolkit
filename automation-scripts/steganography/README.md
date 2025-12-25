# Steganography Module

## script: stego_scan.py

This script combines multiple tools to detect and extract hidden information in images.

### Features
- String analysis
- Metadata inspection (`exiftool`)
- Embedded file detection (`binwalk`)
- Steganography extraction (`steghide` with empty password)

### Usage
From the project root:
```bash
python automation-scripts/steganography/stego_scan.py <image_file>
```

### Dependencies
- `strings`
- `exiftool`
- `binwalk`
- `steghide`
