import unittest
import os
from crystal.core.generate import Generate

class TestGenerate(unittest.TestCase):
    def test_generate_payload(self):
        generator = Generate()
        payload_name = "test_payload.py"
        lhost = "127.0.0.1"
        lport = 4444
        payload_path = generator.run(payload_name, lhost, lport)
        self.assertTrue(os.path.exists(payload_path))
        with open(payload_path, "r") as f:
            content = f.read()
            self.assertIn(lhost, content)
            self.assertIn(str(lport), content)
        os.remove(payload_path)

if __name__ == '__main__':
    unittest.main()
