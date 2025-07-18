from modules.tools.nmap_extended import NmapExtended
from .database import Database

def run_vulnscan(target, alias=None):
    print(f"[*] Running vulnerability scan on {target}...")
    db = Database()
    target_id = db.add_target(target, None, alias)
    nmap = NmapExtended(target)
    result = nmap.run()
    # In a real scenario, we would parse the nmap output and add vulnerabilities to the database
    print(result)
    if alias:
        with open(f"crystal/logs/{alias}_vulnscan.txt", "w") as f:
            f.write(result)
    db.close()
    return result
