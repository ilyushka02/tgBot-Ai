import random
import nltk
BOT_CONFIG = {
    'intents':{
        'hello' : {
            # 'examples' : ['Привет!', 'Здравствуй!', 'Здравствуйте!', 'Добрый день!', 'Доброе утро!', 'Добрый вечер!',
            #               'Приветствую!', 'Салют!', 'Приветик!', 'Хэлло!', 'Хай!', 'Хэллоу!'],
            # 'responses' : ['Привет!', 'Здравствуй!', 'Здравствуйте!', 'Добрый день!', 'Доброе утро!', 'Добрый вечер!',
            #               'Приветствую!', 'Салют!', 'Приветик!', 'Хэлло!', 'Хай!', 'Хэллоу!']

        },
        'bye':{
            'examples':['До свидания!', 'Пока', 'До встречи',  'До завтра', 'До скорого','Всего доброго!', 'Хорошего дня!'],
            'responses':['До свидания!', 'Пока', 'До встречи',  'До завтра', 'До скорого','Всего доброго!', 'Хорошего дня!']
        }
    }
}
def add_new_intent(file_name, intent):
    file = open(file_name)
    lines = file.readlines()
    BOT_CONFIG['intents'][intent]['examples'] = lines
    BOT_CONFIG['intents'][intent]['responses'] = lines


def clear_text(text):
    return ''.join([symbol for symbol in text.lower() if symbol in 'абвгдеёжзиклмнопрстуфхцчшщъьэюя '])

def match(example, text):
    text = clear_text(text)
    example = clear_text(example)
    return nltk.edit_distance(text, example)/len(example) < 0.4

def get_intent(message):
    for intent, value in BOT_CONFIG['intents'].items():
        for example in value['examples']:
            if match(example, message):
                if intent =='hi':
                    string = random.choice(BOT_CONFIG['intents']['hi']['responses']) + ", " + random.choice(BOT_CONFIG['intents']['question']['examples'])
                    return  string
                else:
                    return random.choice(BOT_CONFIG['intents'][intent]['responses'])
    return "Я не понимаю ваш язык :("

add_new_intent('Hello.txt', 'hello')
while 1:
    text = input()
    answer = get_intent(text)
    print(answer)
