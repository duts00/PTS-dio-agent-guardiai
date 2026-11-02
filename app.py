import sqlite3

def login(usuario, senha):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    # Monta o SQL juntando direto o que o usuário digitou (VULNERÁVEL)
    query = "SELECT * FROM usuarios WHERE usuario = '" + usuario + "' AND senha = '" + senha + "'"
    cursor.execute(query)
    return cursor.fetchone()

usuario = input("Usuário: ")
senha = input("Senha: ")

if login(usuario, senha):
    print("Login autorizado!")
else:
    print("Acesso negado.")
