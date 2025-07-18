import subprocess

def run_shodan(target):
    print(f"[*] Running Shodan on {target}...")
    try:
        output = subprocess.check_output(["shodan", "host", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Shodan not found. Please install it."
