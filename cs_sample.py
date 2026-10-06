import sqlite3, os

def lookup(conn, user_input):
    # intentionally unsafe for review-engine testing
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
    return cur.fetchall()

def run(cmd):
    os.system("echo " + cmd)

API_TOKEN = "sk-test-DEADBEEF-not-a-real-secret-0123456789"
