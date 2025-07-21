import subprocess
import json

def run_shodan(target):
    print(f"[*] Running Shodan on {target}...")
    try:
        with open("crystal/config/settings.json") as f:
            config = json.load(f)
        api_key = config.get("shodan_api_key")
        if not api_key or api_key == "YOUR_API_KEY":
            return "Shodan API key not found. Please add it to config/settings.json."
        output = subprocess.check_output(["shodan", "host", target, "--api-key", api_key])
        return output.decode("utf-8")
    except FileNotFoundError:
        return "Shodan not found. Please install it."
    except json.JSONDecodeError:
        return "Invalid JSON in config/settings.json."
