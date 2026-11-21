
from settings import settings
import discord
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as " + str(client.user))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_id = message.author.id
    content = message.content

    if content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')

    elif content.startswith('$smile'):
        await message.channel.send(gen_emodji())

    elif content.startswith('$coin'):
        await message.channel.send(flip_coin())

    elif content.startswith('$pass'):
        await message.channel.send(gen_pass(10))

    # JUEGO DE ADIVINANZAS

    elif content == '$adivina':
        await message.channel.send(start_game(user_id))

    elif content.startswith('$intento'):
        parts = content.split()

        if len(parts) != 2:
            await message.channel.send("Usa: $intento NUMERO")
        else:
            try:
                number = int(parts[1])
                response = guess_number(user_id, number)
                await message.channel.send(response)

            except ValueError:
                await message.channel.send("Debes introducir un número válido.")

    elif content == '$rendirse':
        await message.channel.send(stop_game(user_id))

    else:
        await message.channel.send(
            "No puedo procesar este comando, ¡lo siento!"
        )


client.run(settings["TOKEN"])

