
import pyodbc  # type: ignore
from datetime import datetime

class ReadingResults:
    def __init__(self, server, database, username, password):
        """Initialize the database connection and create the ReadingResults table if it doesn't exist."""
        self.connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the ReadingResults table if it does not already exist."""
        table_creation_query = '''
            IF NOT EXISTS (
                SELECT * FROM sys.tables WHERE name = 'ReadingResults'
            )
            BEGIN
                CREATE TABLE ReadingResults (
                    username NVARCHAR(50),
                    IncorrectWordList NVARCHAR(MAX),
                    DateTimeRead DATETIME
                )
            END
        '''
        self.cursor.execute(table_creation_query)
        self.connection.commit()

    def insert_data(self, username, incorrect_word_list, datetime_read=None):
        """Insert a new record into the ReadingResults table."""
        if datetime_read is None:
            datetime_read = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO ReadingResults (username, IncorrectWordList, DateTimeRead)
            VALUES (?, ?, ?)
        ''', (username, incorrect_word_list, datetime_read))
        self.connection.commit()

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()



