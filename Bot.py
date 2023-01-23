import discord
import Responces
import Token
from discord.ext import commands
from discord import file


async def send_message(message, user_message):
    try:
        responce = Responces.get_responce(user_message)
        if responce == "Abuse":
            await message.delete()
            await message.channel.send(f"{message.author.mention} Please Don't Abuse here")
            await message.author.send("Keep your temper cool relax Don't abuse it's not good")
        else:
            await message.channel.send(responce)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = Token.Token
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='$', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said the following "{user_message}" on ({channel})')

        await send_message(message, user_message)

    client.run(TOKEN)
