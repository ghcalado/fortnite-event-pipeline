import time
import random
from datetime import datetime
from src.database import conectar, salvar_evento
from src.config import SKINS, LOCAIS, ARMAS, RARIDADES, EVENTOS

def rodar_jogo():
    conn, cursor = conectar()
    print("Engine de Eventos Iniciada...")

    try:
        while True:
            evento = random.choice(EVENTOS)
            agora = datetime.now().isoformat()
        
            p, lo, ld, it, ra, vi = [None] * 6

            if evento == "spawn":
                p, lo = random.choice(SKINS), random.choice(LOCAIS)
                print(f"[SPAWN] {p} chegou em {lo}")

            elif evento == "loot":
                p, it, ra = random.choice(SKINS), random.choice(ARMAS), random.choice(RARIDADES)
                print(f"[LOOT] {p} pegou {it} {ra}")

            elif evento == "kill":
                p = random.choice(SKINS)
                vi = random.choice([s for s in SKINS if s != p])
                it = random.choice(ARMAS)
                print(f"[KILL] {p} eliminou {vi} com {it}")

            elif evento == "move":
                p, lo = random.choice(SKINS), random.choice(LOCAIS)
                ld = random.choice([l for l in LOCAIS if l != lo])
                print(f"[MOVE] {p} foi de {lo} para {ld}")
              
            salvar_evento(conn, cursor, (evento, p, lo, ld, it, ra, vi, agora))
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nSaindo do jogo...")
        conn.close()

if __name__ == "__main__":
    rodar_jogo()
