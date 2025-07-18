import unittest
from unittest.mock import patch
from crystal.modules.tools.nmap_extended import run_nmap_scan

class TestNmapExtended(unittest.TestCase):
    @patch('nmap.PortScanner')
    def test_run_nmap(self, mock_port_scanner):
        mock_scanner_instance = mock_port_scanner.return_value
        mock_scanner_instance.csv.return_value = "test output"
        output = run_nmap_scan("example.com")
        self.assertEqual(output, "test output")

if __name__ == '__main__':
    unittest.main()
