import unittest
import os
from crystal.core.report import generate_report

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        alias = "test_alias"
        report_path = generate_report(alias)
        self.assertTrue(os.path.exists(report_path))
        with open(report_path, "r") as f:
            content = f.read()
            self.assertIn(alias, content)
        os.remove(report_path)

if __name__ == '__main__':
    unittest.main()
