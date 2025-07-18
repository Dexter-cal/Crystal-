import subprocess

def run_harvester(target):
    print(f"[*] Running TheHarvester on {target}...")
    try:
        output = subprocess.check_output(["theharvester", "-d", target, "-b", "all"])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "TheHarvester not found. Please install it."
