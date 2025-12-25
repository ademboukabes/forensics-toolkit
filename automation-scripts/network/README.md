# Network Forensics Module

## script: pcap_scan.py

This script automates basic network traffic analysis.

### Features
- Traffic summary (via pyshark)
- HTTP Credential extraction (Authorization headers)
- Potential DNS query analysis (extensible)

### Usage
From the project root:
```bash
python automation-scripts/network/pcap_scan.py <path_to_pcap>
```

### Dependencies
- `pyshark`
- Wireshark/TShark installed on the system
