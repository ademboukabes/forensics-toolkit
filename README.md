#  Forensics Automation Toolkit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A comprehensive Python-based toolkit designed to automate common forensics tasks across Disk, Network, Memory, and Steganography domains. Built for CTFs (Capture The Flag) and initial DFIR (Digital Forensics and Incident Response) investigations.

##  Goal:

- **Automate** standard forensic analysis steps.
- **Accelerate** CTF problem solving.
- **Generate** actionable reports.
- **Demonstrate** structured analysis logic.

##  Project Structure

```
forensics-automation-toolkit/
│
├── automation-scripts/      # Core logic scripts
│   ├── disk/                # Disk forensics (file type, strings, exif)
│   ├── network/             # Network forensics (pcap analysis)
│   ├── memory/              # Memory forensics (volatility3 wrapper)
│   └── steganography/       # Steganography tools wrapper
│
├── samples/                 # Directory to store sample files for testing
├── reports/                 # Generated analysis reports
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

##  Getting Started

### Prerequisites

- **Python 3.8+**
- **External Tools**: Ensure the following are installed and in your PATH:
    - `file` (Linux/Unix)
    - `strings` (Linux/Unix)
    - `exiftool`
    - `binwalk`
    - `foremost`
    - `steghide`
    - `vol` (Volatility 3) or aliased appropriate command

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ademboukabes/forensics-toolkit.git
   cd forensics-toolkit
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

##  Usage

### 1️ Disk Forensics
Analyzes files for type, hashes, strings, and metadata.
```bash
python automation-scripts/disk/disk_scan.py <path_to_image_or_file>
```

### 2️ Network Forensics
Parses PCAP files for traffic summary and credentials.
```bash
python automation-scripts/network/pcap_scan.py <path_to_pcap>
```

### 3️ Memory Forensics
Automates Volatility 3 plugins (pslist, netscan, cmdline).
```bash
python automation-scripts/memory/memory_scan.py <path_to_memory_dump>
```

### 4️ Steganography
Checks for hidden data using strings, exiftool, binwalk, and steghide.
```bash
python automation-scripts/steganography/stego_scan.py <path_to_image>
```

##  Features

| Module | Features | Tools Used |
| :--- | :--- | :--- |
| **Disk** | File type, SHA256, Strings, EXIF | `file`, `strings`, `exiftool` |
| **Network** | Traffic summary, Auth headers, DNS | `pyshark` |
| **Memory** | Processes, Network, Commands | `volatility3` |
| **Stego** | Metadata, Hidden binaries, Pass-less extract | `binwalk`, `steghide`, `strings` |

##  Roadmap

- [ ] **Unified CLI**:Single `forensic.py` entry point.
- [ ] **JSON Reports**: Standardized output format for easy parsing.
- [ ] **Suspect Scoring**: Automated "suspiciousness" rating.
- [ ] **GUI**: Graphical interface using Tkinter or web-based.

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
