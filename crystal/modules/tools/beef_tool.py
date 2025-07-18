import subprocess

def run_beef():
    print(f"[*] Running BeEF...")
    try:
        subprocess.Popen(["beef-xss"])
        return "BeEF started."
    except FileNotFoundError:
        return "BeEF not found. Please install it."
