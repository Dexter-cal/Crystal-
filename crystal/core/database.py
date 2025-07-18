import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('crystal.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS targets (
                id INTEGER PRIMARY KEY,
                ip TEXT,
                domain TEXT,
                alias TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vulnerabilities (
                id INTEGER PRIMARY KEY,
                target_id INTEGER,
                port INTEGER,
                service TEXT,
                vulnerability TEXT,
                FOREIGN KEY (target_id) REFERENCES targets (id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS loot (
                id INTEGER PRIMARY KEY,
                target_id INTEGER,
                type TEXT,
                content TEXT,
                FOREIGN KEY (target_id) REFERENCES targets (id)
            )
        ''')
        self.conn.commit()

    def add_target(self, ip, domain, alias):
        self.cursor.execute("INSERT INTO targets (ip, domain, alias) VALUES (?, ?, ?)", (ip, domain, alias))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_vulnerability(self, target_id, port, service, vulnerability):
        self.cursor.execute("INSERT INTO vulnerabilities (target_id, port, service, vulnerability) VALUES (?, ?, ?, ?)", (target_id, port, service, vulnerability))
        self.conn.commit()

    def add_loot(self, target_id, loot_type, content):
        self.cursor.execute("INSERT INTO loot (target_id, type, content) VALUES (?, ?, ?)", (target_id, loot_type, content))
        self.conn.commit()

    def get_targets(self):
        self.cursor.execute("SELECT * FROM targets")
        return self.cursor.fetchall()

    def get_vulnerabilities(self, target_id):
        self.cursor.execute("SELECT * FROM vulnerabilities WHERE target_id = ?", (target_id,))
        return self.cursor.fetchall()

    def get_loot(self, target_id):
        self.cursor.execute("SELECT * FROM loot WHERE target_id = ?", (target_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
