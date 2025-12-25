import pyshark, sys, os

if len(sys.argv) < 2:
    print("Usage: python pcap_scan.py <pcap_file>")
    sys.exit(1)

# Ensure reports directory exists
os.makedirs("reports", exist_ok=True)

cap = pyshark.FileCapture(sys.argv[1])
creds = []

print("Scanning PCAP...")
for pkt in cap:
    try:
        if 'HTTP' in pkt:
            if 'Authorization' in str(pkt.http):
                creds.append(str(pkt.http))
    except AttributeError:
        # Packet might not have the expected attributes
        pass
    except Exception as e:
        print(f"Error processing packet: {e}")

output_file = "reports/network_report.txt"
with open(output_file,"w") as f:
    for c in creds:
        f.write(c+"\n")

print(f"Report generated at {output_file}")
