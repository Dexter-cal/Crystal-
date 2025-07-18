import unittest
from unittest.mock import patch
from crystal.modules.tools.theharvester import TheHarvester

class TestTheHarvester(unittest.TestCase):
    @patch('subprocess.check_output')
    def test_run_harvester(self, mock_check_output):
        mock_check_output.return_value = b"test output"
        harvester = TheHarvester("example.com")
        output = harvester.run()
        self.assertEqual(output, "test output")

if __name__ == '__main__':
    unittest.main()
