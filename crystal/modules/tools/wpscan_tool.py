import subprocess

def run_wpscan(target):
    print(f"[*] Running Wpscan on {target}...")
    try:
        output = subprocess.check_output(["wpscan", "--url", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Wpscan not found. Please install it."
