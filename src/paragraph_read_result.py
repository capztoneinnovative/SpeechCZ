import pyodbc       # type: ignore  
from datetime import datetime, timedelta

class ReadingResultsDB:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = self.create_connection()

    def create_connection(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password}'
        )
        return conn

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ReadingResults (
            UserID INT,
            ParagraphID INT,
            IncorrectWordList NVARCHAR(MAX),
            CountOfReading INT,
            DateTimeRead DATETIME,
            DurationOfReading TIME
        )
        ''')
        self.connection.commit()

    def insert_data(self, user_id, paragraph_id, incorrect_word_list, count_of_reading,
                    datetime_read, duration_of_reading, score, feedback, device_used, location):
        cursor = self.connection.cursor()
        cursor.execute('''
        INSERT INTO ReadingResults (UserID, ParagraphID, IncorrectWordList, CountOfReading, DateTimeRead,
                                    DurationOfReading)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, paragraph_id, incorrect_word_list, count_of_reading, datetime_read,
              duration_of_reading))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


