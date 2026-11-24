"""Cria lab.db com um usuário de teste, para rodar app.py / app_corrigido.py."""

import sqlite3

conn = sqlite3.connect("lab.db")
conn.execute("DROP TABLE IF EXISTS users")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'troque-isso-123')")
conn.commit()
conn.close()

print("lab.db criado com o usuário 'admin'.")
