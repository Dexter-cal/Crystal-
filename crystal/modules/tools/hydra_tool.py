import subprocess

def run_hydra(target, service, user, password_list):
    print(f"[*] Running Hydra on {target}...")
    try:
        output = subprocess.check_output(["hydra", "-l", user, "-P", password_list, f"{service}://{target}"])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Hydra not found. Please install it."
