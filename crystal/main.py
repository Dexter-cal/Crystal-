# --- main.py ---

import argparse
import os
import subprocess
import json

# Core Modules
from core.vulnscan import run_vulnscan
from core.exploit_suggester import suggest_exploit
from core.auto_exploit import auto_exploit
from core.exploit_chain import run_exploit_chain
from core.generate import generate_payload
from core.report import generate_report

# Utility Modules
from utils.banner import get_random_banner

# Attack Modules
from modules.attack.phishing_emailer import launch_phishing_email
from modules.post_exploit.screen import screen_record
from modules.post_exploit.keylogger import keylogger
from modules.evidence.cleaner import clean_logs
from modules.evidence.persistence import set_persistence

# Tool Modules
from modules.tools.nmap_extended import run_nmap_scan
from modules.tools.whatweb_tool import run_whatweb
from modules.tools.dirb_tool import run_dirb
from modules.tools.wpscan_tool import run_wpscan
from modules.tools.shodan_tool import run_shodan
from modules.tools.netcat import run_netcat
from modules.tools.theharvester import run_harvester
from modules.tools.amass import run_amass
from modules.tools.sublist3r_tool import run_sublist3r
from modules.tools.dnsenum_tool import run_dnsenum
from modules.tools.nikto_tool import run_nikto
from modules.tools.beef_tool import run_beef
from modules.tools.fatrat_tool import run_fatrat
from modules.tools.john_tool import run_john
from modules.tools.sqlmap_tool import run_sqlmap
from modules.tools.hydra_tool import run_hydra
from modules.tools.aircrack_tool import run_aircrack
from modules.tools.msfconsole_tool import run_msfconsole
from modules.tools.androrat_tool import run_androrat

CONFIG_PATH = "config/settings.json"

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {}

def main():
    banner = get_random_banner()
    print(banner)

    parser = argparse.ArgumentParser(description="Crystal - Modular Red Teaming Framework")
    parser.add_argument("--target", help="Target IP or domain")
    parser.add_argument("--alias", help="Alias for the operation")
    parser.add_argument("--scan", action="store_true", help="Run vulnerability scan")
    parser.add_argument("--suggest", action="store_true", help="Suggest exploit")
    parser.add_argument("--exploit-chain", action="store_true", help="Run exploit chain")
    parser.add_argument("--auto", action="store_true", help="Run auto exploit chain")
    parser.add_argument("--generate", action="store_true", help="Generate payload")
    parser.add_argument("--report", action="store_true", help="Generate report")
    parser.add_argument("--screenrecord", action="store_true", help="Start screen recording")
    parser.add_argument("--keylog", action="store_true", help="Start keylogger")
    parser.add_argument("--clean", action="store_true", help="Clear logs")
    parser.add_argument("--persist", action="store_true", help="Enable persistence")
    parser.add_argument("--phish", action="store_true", help="Launch phishing email")
    parser.add_argument("--tool", help="Run tool module (e.g., nmap, dirb, shodan, john)")
    args = parser.parse_args()

    if args.scan:
        run_vulnscan(args.target, alias=args.alias)

    if args.suggest:
        suggest_exploit(args.target)

    if args.exploit_chain:
        run_exploit_chain(args.target)

    if args.auto:
        dummy_services = [
            {"port": 80, "name": "apache", "version": "2.4.49"},
            {"port": 21, "name": "vsftpd", "version": "3.0.3"}
        ]
        auto_exploit(args.target, dummy_services, auto_attack=True)

    if args.generate:
        platform = input("Platform (python/windows/linux/android): ")
        lhost = input("LHOST: ")
        lport = input("LPORT: ")
        obfuscate = input("Obfuscate (y/n): ").lower() == "y"
        generate_payload(platform, lhost, lport, obfuscate=obfuscate)

    if args.report:
        generate_report(args.alias or "unknown")

    if args.screenrecord:
        screen_record(args.target)

    if args.keylog:
        keylogger(args.target)

    if args.clean:
        clean_logs(args.target)

    if args.persist:
        set_persistence(args.target)

    if args.phish:
        launch_phishing_email(args.target)

    if args.tool:
        tool_map = {
            "nmap": run_nmap_scan,
            "whatweb": run_whatweb,
            "dirb": run_dirb,
            "wpscan": run_wpscan,
            "shodan": run_shodan,
            "netcat": run_netcat,
            "harvester": run_harvester,
            "amass": run_amass,
            "sublist3r": run_sublist3r,
            "dnsenum": run_dnsenum,
            "nikto": run_nikto,
            "beef": run_beef,
            "fatrat": run_fatrat,
            "john": lambda: run_john(input("Hash file: ")),
            "sqlmap": run_sqlmap,
            "hydra": lambda: run_hydra(args.target, input("Service: "), input("User: "), input("Password list: ")),
            "aircrack": lambda: run_aircrack(input("PCAP file: ")),
            "msf": run_msfconsole,
            "androrat": run_androrat
        }
        if args.tool.lower() in tool_map:
            tool_map[args.tool.lower()]()
        else:
            print(f"[!] Unknown tool: {args.tool}")

if __name__ == "__main__":
    main()
