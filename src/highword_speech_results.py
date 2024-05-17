import pyodbc  # type: ignore
from datetime import datetime

class DatabaseHandler:
    def __init__(self, server, database, username, password):
        self.connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='results' and xtype='U')
                               CREATE TABLE results (
                                   high_freq_word NVARCHAR(255),
                                   correct_count INT,
                                   incorrect_count INT,
                                   total_attempts INT,
                                   accuracy_rate FLOAT,
                                   last_attempt_date DATETIME)''')
        self.connection.commit()

    def insert_result(self, high_freq_word, correct_count, incorrect_count, total_attempts, accuracy_rate):
        last_attempt_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''INSERT INTO results (high_freq_word, correct_count, incorrect_count, total_attempts, accuracy_rate, last_attempt_date)
                               VALUES (?, ?, ?, ?, ?, ?)''', 
                               (high_freq_word, correct_count, incorrect_count, total_attempts, accuracy_rate, last_attempt_date))
        self.connection.commit()

    def close(self):
        self.connection.close()


