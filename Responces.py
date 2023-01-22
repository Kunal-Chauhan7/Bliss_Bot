import random
import requests
import json
from Token import quote_api as qpi
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
        full_quote = '"'+quoteText+'"' +"\n\n By : "+quoteAuthor
        return full_quote
banned_words = ['chutiya', 'gandu', 'bhenchod', 'madarchod', 'bakchod', 'kamina', 'chodu', 'bhosdike', 'harami', 'lodu',
                'arse', 'arsehead', 'arsehole', 'ass', 'asshole', 'bastard', 'bitch', 'bloody', 'bollocks',
                'brotherfucker', 'bugger', 'cock', 'cocksucker', 'cunt', 'dick', 'dickhead', 'frigger', 'fuck',
                'motherfucker', 'nigga', 'prick', 'pussy', 'slut', 'son of a bitch', 'son of a whore', 'wanker']

head_tails = ["head", "Tails", ]
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
    if p_message == '$hello':
        return 'Hey Hey!!'
    if p_message == 'roll':
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
    elif p_message[0] == '$':
        return random_list[random_message_index]
