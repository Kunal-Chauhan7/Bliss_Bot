import discord
import Responces
import Token
from discord.ext import commands
from waifu import WaifuClient

waifu = WaifuClient()


def run_discord_bot():
    TOKEN = Token.Token
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='$', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    async def send_message(message, user_message):
        try:
            responce = Responces.get_responce(user_message)
            if responce == "Abuse":
                await message.delete()
                await message.channel.send(f"{message.author.mention} Please Don't Abuse here")
                await message.author.send("Keep your temper cool relax Don't abuse it's not good")
            if responce.startswith("$waifu"):
                if responce.endswith('u' or ' '):
                    category = 'waifu'
                else:
                    category = responce.split()[1]
                waifu_pic: str = waifu.sfw(category=category)
                await message.channel.send(waifu_pic)
            if responce.startswith("$nsfw"):
                if responce.endswith('w' or ' '):
                    category = 'waifu'
                else:
                    category = responce.split()[1]
                waifu_pic: str = waifu.nsfw(category=category)
                await message.channel.send(waifu_pic)
            if responce.startswith('$kitty'):
                await message.channel.send('https://cataas.com/cat')
            if responce.startswith('$ping'):
                await message.channel.send(f'@everyone {responce[6:]}')
            if responce.startswith('$msg'):
                raw_target = responce.split()[1][2:]
                target_user = raw_target[:len(raw_target)-1]
                dm_user = await client.fetch_user(target_user)
                raw_msg = responce.split()[2:]
                msg = " "
                msg = msg.join(raw_msg)
                await dm_user.send(msg)
            else:
                await message.channel.send(responce)

        except Exception as e:
            print(e)

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
