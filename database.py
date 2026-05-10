import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conn.cursor()
    
    #Users Table

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        return self.cursor.fetchone()
    def register_user(self, username, password_hash):
        self.cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        self.conn.commit()

    #Transactions Table

    def add_transaction(self, user_id, transaction_type, category, amount):
        self.cursor.execute(
            "INSERT INTO transactions (user_id, transaction_type, category, amount) VALUES (%s, %s, %s, %s)",
            (user_id, transaction_type, category, amount)
        )
        self.conn.commit()
    
    def get_all_transactions(self, user_id):
        self.cursor.execute(
            "SELECT * FROM transactions WHERE user_id = %s", (user_id,))
        return self.cursor.fetchall()
    
    def update_transactions(self, id, user_id, transaction_type, category, amount):
        self.cursor.execute(
            "UPDATE transactions SET user_id=%s, transaction_type=%s, category=%s, amount=%s WHERE id=%s",
            (user_id, transaction_type, category, amount, id))
        self.conn.commit()

    def delete_transactions(self, id):
        self.cursor.execute(
            "DELETE FROM transactions WHERE id=%s", (id,))
        self.conn.commit()
