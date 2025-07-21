import os
from .database import Database

def generate_report(alias):
    print(f"[*] Generating report for {alias}...")
    db = Database()
    targets = db.get_targets()
    report_path = os.path.join("crystal", "logs", f"{alias}_report.txt")
    with open(report_path, "w") as f:
        f.write(f"Report for {alias}\n\n")
        for target in targets:
            if target[3] == alias:
                target_id = target[0]
                f.write(f"Target: {target[1]} ({target[2]})\n")
                vulnerabilities = db.get_vulnerabilities(target_id)
                if vulnerabilities:
                    f.write("Vulnerabilities:\n")
                    for vulnerability in vulnerabilities:
                        f.write(f"  - Port {vulnerability[2]} ({vulnerability[3]}): {vulnerability[4]}\n")
                loot = db.get_loot(target_id)
                if loot:
                    f.write("Loot:\n")
                    for item in loot:
                        f.write(f"  - {item[2]}: {item[3]}\n")
    db.close()
    print(f"[+] Report generated at {report_path}")
    return report_path
