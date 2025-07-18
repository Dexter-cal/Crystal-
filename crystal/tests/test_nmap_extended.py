import unittest
from unittest.mock import patch
from crystal.modules.tools.nmap_extended import NmapExtended

class TestNmapExtended(unittest.TestCase):
    @patch('subprocess.check_output')
    def test_run_nmap(self, mock_check_output):
        mock_check_output.return_value = b"test output"
        nmap = NmapExtended("example.com")
        output = nmap.run()
        self.assertEqual(output, "test output")

if __name__ == '__main__':
    unittest.main()
