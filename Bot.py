import discord
import Responces
import Token

async def send_message(message, user_message, is_private):
    try:
        responce = Responces.get_responce(user_message)
        await message.author.send(responce) if is_private else await message.channel.send(responce)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = Token.Token
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

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
        if user_message[0] == '$':
            user_message = user_message[1:]
            await send_message(message,user_message,is_private=False)
        else:
            await send_message(message,user_message,is_private=True)

    client.run(TOKEN)