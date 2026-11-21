
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["😀", "🙂", "😆", "🤣"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 1)

    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"


# JUEGO DE ADIVINANZAS

games = {}


def start_game(user_id):
    if user_id in games:
        return "Ya tienes una partida activa."

    games[user_id] = {
        "number": random.randint(1, 100),
        "attempts": 0
    }

    return "🎮 ¡Nueva partida! Adivina el número del 1 al 100."


def guess_number(user_id, number):
    if user_id not in games:
        return "Primero inicia una partida con $adivina."

    if number < 1 or number > 100:
        return "El número debe estar entre 1 y 100."

    game = games[user_id]
    game["attempts"] += 1

    secret = game["number"]

    if number < secret:
        return "📈 ¡Más alto!"

    elif number > secret:
        return "📉 ¡Más bajo!"

    else:
        attempts = game["attempts"]
        del games[user_id]

        return "🏆 ¡Acertaste! Lo conseguiste en " + str(attempts) + " intentos."


def stop_game(user_id):
    if user_id not in games:
        return "No tienes ninguna partida activa."

    number = games[user_id]["number"]
    del games[user_id]

    return "Partida terminada. El número era " + str(number) + "."
