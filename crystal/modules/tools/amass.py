import subprocess

def run_amass(target):
    print(f"[*] Running Amass on {target}...")
    try:
        output = subprocess.check_output(["amass", "enum", "-d", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Amass not found. Please install it."
