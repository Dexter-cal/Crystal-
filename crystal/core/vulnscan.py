from modules.tools.nmap_extended import run_nmap_scan
from .database import Database
import csv

def run_vulnscan(target, alias=None):
    print(f"[*] Running vulnerability scan on {target}...")
    db = Database()
    target_id = db.add_target(target, None, alias)
    result = run_nmap_scan(target)

    # Parse the CSV output from nmap
    reader = csv.reader(result.splitlines())
    for row in reader:
        if len(row) >= 7 and row[0] != 'host':
            ip = row[0]
            port = row[3]
            service = row[5]
            version = row[6]
            db.add_vulnerability(target_id, port, service, version)

    if alias:
        with open(f"crystal/logs/{alias}_vulnscan.txt", "w") as f:
            f.write(result)
    db.close()
    return result
