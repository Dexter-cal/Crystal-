from modules.tools.nmap_extended import NmapExtended

def run_vulnscan(target, alias=None):
    print(f"[*] Running vulnerability scan on {target}...")
    nmap = NmapExtended(target)
    result = nmap.run()
    print(result)
    if alias:
        with open(f"crystal/logs/{alias}_vulnscan.txt", "w") as f:
            f.write(result)
    return result
