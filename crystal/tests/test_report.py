import unittest
import os
from crystal.core.report import Report

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        target = "test_target"
        report = Report(target)
        report.add_finding("Test finding 1")
        report.add_finding("Test finding 2")
        report_path = report.generate()
        self.assertTrue(os.path.exists(report_path))
        with open(report_path, "r") as f:
            content = f.read()
            self.assertIn(target, content)
            self.assertIn("Test finding 1", content)
            self.assertIn("Test finding 2", content)
        os.remove(report_path)

if __name__ == '__main__':
    unittest.main()
