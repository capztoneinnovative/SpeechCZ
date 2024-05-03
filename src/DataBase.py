import sys
import pyodbc            # type: ignore

from error_handling import CustomException
from logger import logging


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
            logging.info("Connected to the database successfully!")
            #print("Connected to the database successfully!")
            return self.connection
        except Exception as e:
            logging.error("Error inserting data:", exc_info=True)
            #print("Error connecting to database:", e)
            raise CustomException(e,sys)
            #return None

    def close(self):
        if self.connection:
            self.connection.close()
            #print("Connection closed.")
  

    