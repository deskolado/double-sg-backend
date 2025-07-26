import random
from datetime import datetime

def gerar_sinal():
    return {
        "cor": random.choice(["VERMELHO", "PRETO"]),
        "horario": datetime.now().strftime("%H:%M"),
        "confianca": "99.4%",
        "armadilha": False
    }

def gerar_sinal_branco():
    return {
        "branco": True,
        "chance": "99.1%",
        "melhor_horario": datetime.now().strftime("%H:%M")
    }
