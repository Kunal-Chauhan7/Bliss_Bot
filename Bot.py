import discord
import Responces
import Token
from discord.ext import commands
from waifu import WaifuClient
import requests
import random

#nsfw = waifu neko trap blowjob
#sfw = waifu neko shinobu megumin bully cuddle cry hug awoo kiss lick pat smug bonk yeet blush smile wave highfive
# handhold nom bite glomp slap kill kick happy wink poke dance cringe
anime_commands = ['cuddle', 'feed', 'handhold', 'highfive', 'hug', 'kick','kiss' ,'poke', 'punch',
                  'shoot', 'bite', 'tickle','wave', 'wink', 'yeet', 'slap', 'pat', 'stare']

waifu = WaifuClient()
def love_calc():
    love = random.randrange(100)
    return love
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
            for i in anime_commands:
                if i in responce:
                    resp = requests.get(f"https://nekos.best/api/v2/{i}")
                    data = resp.json()
                    await message.channel.send(data["results"][0]["url"])
                    await message.channel.send(f"{message.author.mention} {i} on {responce.split()[1]}")
            if responce.startswith('$ship'):
                love = love_calc()
                await message.channel.send(love)
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
                await dm_user.send(f'*{message.author.name}*  said  `{msg}` on **{message.channel.name}** to you')
            else:
                await message.channel.send(responce)

        except Exception as e:
            print(e)

    @client.event
    async def on_message(message):
        if message.content.startswith('$'):
            if message.author == client.user:
                return
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            print(f'{username} said the following "{user_message}" on ({channel})')
            await send_message(message, user_message)

    client.run(TOKEN)
