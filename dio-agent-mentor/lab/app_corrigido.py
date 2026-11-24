"""
app_corrigido.py — mesma função de login, corrigida com consulta
parametrizada. O driver sqlite3 trata o valor como dado, nunca como
parte do comando SQL, então o payload de SQL Injection deixa de
funcionar — ele é comparado literalmente, não interpretado.
"""

import sqlite3

DB_PATH = "lab.db"


def login(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # CORRIGIDO: placeholders (?) em vez de concatenar a string.
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    row = cursor.fetchone()

    conn.close()
    return row is not None


if __name__ == "__main__":
    print("Login normal:", login("admin", "senha_errada"))

    payload_usuario = "admin' OR '1'='1' --"
    print("Login com payload de SQLi (deve ser False agora):", login(payload_usuario, "qualquer_coisa"))
