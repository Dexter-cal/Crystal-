import unittest
from unittest.mock import patch
from crystal.modules.tools.theharvester import run_harvester

class TestTheHarvester(unittest.TestCase):
    @patch('subprocess.check_output')
    def test_run_harvester(self, mock_check_output):
        mock_check_output.return_value = b"test output"
        output = run_harvester("example.com")
        self.assertEqual(output, "test output")

if __name__ == '__main__':
    unittest.main()
