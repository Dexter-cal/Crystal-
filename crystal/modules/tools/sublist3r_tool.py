import subprocess

def run_sublist3r(target):
    print(f"[*] Running Sublist3r on {target}...")
    try:
        output = subprocess.check_output(["sublist3r", "-d", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Sublist3r not found. Please install it."
