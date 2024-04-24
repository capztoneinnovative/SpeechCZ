import pandas as pd                      # type: ignore
import pyodbc                            # type: ignore

from DataBase import DataBase
from logger import logging
from error_handling import CustomException

## Insert High frequency word excel file in Db_table

def insert_data_to_database(connection, df, table_name):
    try:
        cursor = connection.cursor()
        for index, row in df.iterrows():
            values = tuple(row)
            placeholders = ",".join(["?" for _ in range(len(values))])
            sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(sql, values)
        connection.commit()
        logging.info("Data inserted successfully!")
    except pyodbc.Error as e:
        logging.error("Error inserting data:", exc_info=True)
        
        
## insert Image and Longtext(story) in Db_table

def insert_file(connection, image_path, text_path):
    try:
        cursor = connection.cursor()
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        with open(text_path, 'r', encoding='utf-8') as text_file:
            text_data = text_file.read()
        cursor.execute("INSERT INTO imgtxt (ImageData, TextData) VALUES (?, ?)", pyodbc.Binary(image_data), text_data)
        connection.commit()
        logging.info("Files inserted successfully.")
    except pyodbc.Error as e:
        logging.error("Error inserting files:", exc_info=True)
        
        
    