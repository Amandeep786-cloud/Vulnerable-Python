import sqlite3

def search_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

username = input("Enter username: ")
user_info = search_user(username)
print("User info:", user_info)
