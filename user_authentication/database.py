import sqlite3

class Database():
    def __init__(self):
        self.conn= sqlite3.connect("database.db")
        self.cursor= self.conn.cursor()
        self.create_user_table()
    def create_user_table(self):
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username varchar(255) UNIQUE,
                    email varchar(255) UNIQUE,
                    password varchar(255)
                )
            '''
        )
        self.conn.commit()
        
    def create_user(self, username, email, password):
        self.cursor.execute("INSERT INTO users(username, email, password) VALUES(?, ?, ?)", (username, email, password))
        self.conn.commit()
        
    def get_users(self):
        users= self.cursor.execute("SELECT * FROM users").fetchall()
        return users
    
    def get_user(self, user_id):
        user= self.cursor.execute("SELECT * FROM users WHERE id= ?", (user_id,)).fetchall()
        return user
    
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id= ?", (user_id,))
        self.conn.commit()
        
    def update_user(self, user_id, username, email):
        self.cursor.execute("UPDATE users SET username= ?, email= ? WHERE id= ?", (username, email, user_id))
        self.conn.commit()
        
        user= self.cursor.execute("SELECT * FROM users WHERE id= ?", (user_id, ))
        self.conn.commit()
        return user
    def login(self, username, password):
        user= self.cursor.execute("SELECT * FROM users WHERE username= ? AND password= ?", (username, password)).fetchone()
        return user
    
    def close_connection(self):
        self.conn.close()
    
    