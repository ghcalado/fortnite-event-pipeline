import sqlite3

def conectar():
    # Salva dentro de uma pasta chamada data
    conn = sqlite3.connect("data/fortnite.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabela_eventos (
            evento TEXT, personagem TEXT, local_origem TEXT, 
            local_destino TEXT, item TEXT, raridade TEXT, 
            vitima TEXT, tempo TEXT
        )
    ''')
    return conn, cursor

def salvar_evento(conn, cursor, dados):
    cursor.execute('INSERT INTO tabela_eventos VALUES (?,?,?,?,?,?,?,?)', dados)
    conn.commit()
