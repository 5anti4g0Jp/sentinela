"""
app.py de laboratório — login com SQL Injection, de propósito.

Objetivo: servir de caso de teste para a skill `vulnerability-analysis`.
NÃO use este padrão fora de laboratório. Veja app_corrigido.py para a
versão corrigida com consulta parametrizada.

Como testar sozinho (sem precisar de servidor web):
    python3 lab/seed_db.py      # cria lab.db com um usuário de teste
    python3 lab/app.py          # tenta logins e mostra o resultado
"""

import sqlite3

DB_PATH = "lab.db"


def login(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # VULNERÁVEL: a entrada do usuário é concatenada direto na query.
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )
    cursor.execute(query)
    row = cursor.fetchone()

    conn.close()
    return row is not None


if __name__ == "__main__":
    print("Login normal:", login("admin", "senha_errada"))

    # Payload clássico de SQL Injection: comenta o resto da query e
    # força a condição a ser sempre verdadeira.
    payload_usuario = "admin' OR '1'='1' --"
    print("Login com payload de SQLi:", login(payload_usuario, "qualquer_coisa"))
