import subprocess

def run_dnsenum(target):
    print(f"[*] Running Dnsenum on {target}...")
    try:
        output = subprocess.check_output(["dnsenum", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Dnsenum not found. Please install it."
