from pyrogram import Client, filters

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"🔄`{prefix_userbot}swap`"
ccomand = " Изменяет раскладку текста."


def command_swap(app):
    @app.on_message(filters.command("swap", prefixes=prefix_userbot))
    def swap(_, message):
        original_text = message.reply_to_message.text
        swapped_text = swap_layout(original_text)
        message.reply_text(swapped_text)

eng_to_rus = str.maketrans(
    "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?~`!@#$%^&*()_+",
    "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ёё!\"№;%:?*()_+"
)
rus_to_eng = str.maketrans(
    "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ёё!\"№;%:?*()_+",
    "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?~`!@#$%^&*()_+"
)


def swap_layout(text):
    words = text.split()
    swapped_words = []
    for word in words:
        if word.isupper():
            swapped_word = word.lower().translate(
                rus_to_eng if 'а' <= word.lower()[0] <= 'я' or word.lower()[0] == 'ё' else eng_to_rus)
            swapped_words.append(swapped_word.upper())
        else:
            swapped_words.append(
                word.translate(rus_to_eng if 'а' <= word.lower()[0] <= 'я' or word.lower()[0] == 'ё' else eng_to_rus))
    return ' '.join(swapped_words)


print("Модуль swap загружен!")
