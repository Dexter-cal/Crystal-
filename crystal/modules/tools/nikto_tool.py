import subprocess

def run_nikto(target):
    print(f"[*] Running Nikto on {target}...")
    try:
        output = subprocess.check_output(["nikto", "-h", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Nikto not found. Please install it."
