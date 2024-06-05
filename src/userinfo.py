import pyodbc                       #type: ignore
import datetime

class UserHandler:
    def __init__(self, server, database, username, password):
        try:
            self.connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={username};'
                f'PWD={password};'
            )
            print("Connection established successfully.")
        except pyodbc.Error as e:
            print("An error occurred while connecting to the database:", e)

    def register_user(self, username, email, full_name, dob, gender):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO [User] (Username, Email, FullName, DOB, Gender) VALUES (?, ?, ?, ?, ?)"
            data = (username, email, full_name, dob, gender)
            cursor.execute(query, data)
            self.connection.commit()
            cursor.close()
            print("User registered successfully.")
        except pyodbc.Error as e:
            print("An error occurred while registering the user:", e)

    def login_user(self, username, password):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM [User] WHERE Username = ? AND Passwords = ?"
            data = (username, password)
            cursor.execute(query, data)
            user = cursor.fetchone()
            cursor.close()
            if user:
                print("Login successful.")
                return True
            else:
                print("Invalid username or password.")
                return False
        except pyodbc.Error as e:
            print("An error occurred while logging in:", e)
            return False

    def update_user_info(self, user_id, new_email=None, new_full_name=None, new_dob=None, new_gender=None):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE [User] SET "
            updates = []
            if new_email:
                updates.append("Email = ?")
            if new_full_name:
                updates.append("FullName = ?")
            if new_dob:
                updates.append("DOB = ?")
            if new_gender:
                updates.append("Gender = ?")
            query += ", ".join(updates)
            query += " WHERE UID = ?"
            data = []
            if new_email:
                data.append(new_email)
            if new_full_name:
                data.append(new_full_name)
            if new_dob:
                data.append(new_dob)
            if new_gender:
                data.append(new_gender)
            data.append(user_id)
            cursor.execute(query, data)
            self.connection.commit()
            cursor.close()
            last_updated = datetime.datetime.now()
            print(f"User {user_id} information updated at {last_updated}.")
        except pyodbc.Error as e:
            print("An error occurred while updating user information:", e)
            
    
