import subprocess

def run_androrat():
    print(f"[*] Running Androrat...")
    try:
        subprocess.Popen(["androrat"])
        return "Androrat started."
    except FileNotFoundError:
        return "Androrat not found. Please install it."
