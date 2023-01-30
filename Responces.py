import random
import requests
import json
from Token import quote_api as qpi
import anime_images_api
anime = anime_images_api.Anime_Images()
anime_command_list = ['baka', 'bite', 'blush', 'bored', 'cry', 'cuddle', 'dance', 'facepalm', 'feed', 'handhold',
                      'happy', 'highfive', 'hug', 'kick','kiss', 'laugh', 'nod', 'nom', 'nope', 'pat', 'poke'
    , 'pout', 'punch', 'shoot', 'shrug', 'slap', 'sleep', 'smile', 'smug', 'stare', 'think', 'thumbsup', 'tickle',
                      'wave', 'wink', 'yeet','husbando', 'kitsune', 'neko', 'waifu']
def jokes():
    f = r"https://official-joke-api.appspot.com/random_joke"
    data = requests.get(f)
    tt = json.loads(data.text)
    jokee = tt['setup'] + '\n\n' + tt['punchline']
    return jokee
def quote(category = 'happiness'):
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': qpi})
    if response.status_code == requests.codes.ok:
        result = json.loads(response.text)
        quoteText = result[0]['quote']
        quoteAuthor = result[0]['author']

        full_quote = f'Here is a Quote on {category}\n\n"{quoteText}"\nBy : {quoteAuthor}'
        return full_quote
def weather(city = 'New Delhi'):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': qpi})
    if response.status_code == requests.codes.ok:
        result = json.loads(response.text)
        weather = f"Place : {city}\nTemp : {result['temp']}\nHumidity : {result['humidity']}\nMin Temp : {result['min_temp']}\nMax Temp : {result['max_temp']}\nWind Speed : {result['wind_speed']}"
        return weather
banned_words = ['chutiya', 'gandu', 'bhenchod', 'madarchod', 'bakchod', 'kamina', 'chodu', 'bhosdike', 'harami', 'lodu',
                'arse', 'arsehead', 'arsehole', 'ass', 'asshole', 'bastard', 'bitch', 'bloody', 'bollocks',
                'brotherfucker', 'bugger', 'cock', 'cocksucker', 'cunt', 'dick', 'dickhead', 'frigger', 'fuck',
                'motherfucker', 'nigga', 'prick', 'pussy', 'slut', 'son of a bitch', 'son of a whore', 'wanker']

head_tails = ["head", "Tails", ]
anime_command = ['$hug','$kiss','$slap','$wink','$kill','$pat','$cuddle']
anime_command_nsfw = ['$boobs','$hentai']
random_list = [
    "Please try writing something more descriptive.",
    "Oh! It appears you wrote something I don't understand yet",
    "Do you mind trying to rephrase that?",
    "I'm terribly sorry, I didn't quite catch that.",
    "I can't answer that yet, please try asking something else."
]


def get_responce(message: str) -> str:
    p_message = message.lower()
    for word in banned_words:
        if word in p_message:
            return "Abuse"
    for animes in anime_command:
        if animes in p_message:
            res = anime.get_sfw(animes[1:])
            return res
    for nsfw_animes in anime_command_nsfw:
        if nsfw_animes in p_message:
            res = anime.get_nsfw(nsfw_animes[1:])
            return res

    if p_message == '$hello':
        return 'Hey Hey!!'
    if p_message == '$roll':
        return str(random.randint(1, 6))
    if p_message == '$help':
        return '`this will be the help message`'
    if p_message == '$flip':
        result_h_t = random.randrange(len(head_tails))
        return head_tails[result_h_t]
    if p_message == '$test':
        return 'everything is fine ig'
    if p_message == '$bye':
        return 'Have a great Day Ahead'
    random_message_index = random.randrange(len(random_list))
    if p_message == '$joke':
        return jokes()
    if p_message[0:6] == '$quote':
        return quote(p_message[7:])
    if p_message[0:8] == '$weather':
        return weather(p_message[8:])
    if p_message == '$ping':
        return 'pong'
    if p_message.startswith('$waifu'):
        return p_message
    if p_message.startswith('$nsfw'):
        return p_message
    if p_message.startswith('$kitty'):
        return p_message
    if p_message.startswith('$ping'):
        return p_message
    elif p_message[0] == '$':
        return random_list[random_message_index]
