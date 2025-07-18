import subprocess

def run_dirb(target):
    print(f"[*] Running Dirb on {target}...")
    try:
        output = subprocess.check_output(["dirb", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Dirb not found. Please install it."
