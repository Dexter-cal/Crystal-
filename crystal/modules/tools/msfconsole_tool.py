import subprocess

def run_msfconsole():
    print(f"[*] Running Metasploit Framework...")
    try:
        subprocess.Popen(["msfconsole"])
        return "Metasploit Framework started."
    except FileNotFoundError:
        return "Metasploit Framework not found. Please install it."
