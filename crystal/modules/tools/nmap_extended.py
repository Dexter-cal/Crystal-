import subprocess

def run_nmap_scan(target):
    print(f"[*] Running Nmap scan on {target}...")
    try:
        output = subprocess.check_output(["nmap", "-sV", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Nmap not found. Please install it."
