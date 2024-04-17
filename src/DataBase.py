import pyodbc

class DataBase:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
            print("Connected to the database successfully!")
            return self.connection
        except pyodbc.Error as e:
            print("Error connecting to database:", e)
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
