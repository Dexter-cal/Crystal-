import nmap

def run_nmap_scan(target):
    print(f"[*] Running Nmap scan on {target}...")
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sV')
    return nm.csv()
