import subprocess

def run_aircrack(pcap_file):
    print(f"[*] Running Aircrack-ng on {pcap_file}...")
    try:
        output = subprocess.check_output(["aircrack-ng", pcap_file])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Aircrack-ng not found. Please install it."
