import subprocess

def run_sqlmap(url):
    print(f"[*] Running Sqlmap on {url}...")
    try:
        output = subprocess.check_output(["sqlmap", "-u", url, "--batch"])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Sqlmap not found. Please install it."
