from googletrans import Translator
#-*- coding: UTF-8 -*-

while True:
    selection = input('''[[ Thanks for using Translator App.The translate engine is provided by Google Translator ]]\n
    1. Chinese - English\n
    2. English - Chinese\n
    3. Quit\n''')
    if selection == '1':
        key_words = input("Please input words or sentences you want to translate:")
        translator = Translator()
        result = translator.translate(key_words,dest='en').text
        print(result)
    elif selection == '2':
        key_words = input("Please input words or sentences you want to translate:")
        translator = Translator()
        result = translator.translate(key_words,dest='zh-CN').text
        print(result)
    elif selection == '3':
        print("Thanks for using this system. Bye")
        break
