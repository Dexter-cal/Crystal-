import subprocess

def run_fatrat():
    print(f"[*] Running TheFatRat...")
    try:
        subprocess.Popen(["fatrat"])
        return "TheFatRat started."
    except FileNotFoundError:
        return "TheFatRat not found. Please install it."
