import unittest
import os
from crystal.core.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db.close()
        os.remove('crystal.db')

    def test_add_target(self):
        target_id = self.db.add_target('127.0.0.1', 'localhost', 'test')
        self.assertEqual(target_id, 1)
        targets = self.db.get_targets()
        self.assertEqual(len(targets), 1)
        self.assertEqual(targets[0][1], '127.0.0.1')

    def test_add_vulnerability(self):
        target_id = self.db.add_target('127.0.0.1', 'localhost', 'test')
        self.db.add_vulnerability(target_id, 80, 'http', 'Test vulnerability')
        vulnerabilities = self.db.get_vulnerabilities(target_id)
        self.assertEqual(len(vulnerabilities), 1)
        self.assertEqual(vulnerabilities[0][3], 'http')

    def test_add_loot(self):
        target_id = self.db.add_target('127.0.0.1', 'localhost', 'test')
        self.db.add_loot(target_id, 'password', 'test_password')
        loot = self.db.get_loot(target_id)
        self.assertEqual(len(loot), 1)
        self.assertEqual(loot[0][2], 'password')

if __name__ == '__main__':
    unittest.main()
