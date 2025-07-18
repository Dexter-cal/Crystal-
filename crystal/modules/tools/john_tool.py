import subprocess

def run_john(hash_file):
    print(f"[*] Running John the Ripper on {hash_file}...")
    try:
        output = subprocess.check_output(["john", hash_file])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "John the Ripper not found. Please install it."
