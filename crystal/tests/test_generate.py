import unittest
import os
from crystal.core.generate import generate_payload

class TestGenerate(unittest.TestCase):
    def test_generate_payload(self):
        payload_name = "test_payload.py"
        lhost = "127.0.0.1"
        lport = 4444
        platform = "python"
        payload_path = generate_payload(platform, lhost, lport)
        self.assertTrue(os.path.exists(payload_path))
        with open(payload_path, "r") as f:
            content = f.read()
            self.assertIn(lhost, content)
            self.assertIn(str(lport), content)
        os.remove(payload_path)

if __name__ == '__main__':
    unittest.main()
