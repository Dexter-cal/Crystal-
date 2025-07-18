import subprocess

def run_whatweb(target):
    print(f"[*] Running WhatWeb on {target}...")
    try:
        output = subprocess.check_output(["whatweb", target])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "WhatWeb not found. Please install it."
