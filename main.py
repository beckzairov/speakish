"""

This is a echo bot.

It echoes any incoming text messages.

"""


import logging

from aiogram import Bot, Dispatcher, executor, types

from oxfordLookup import getDefinitions

from googletrans import Translator

translator = Translator()


API_TOKEN = '6006939825:AAEDmhsnTUdKoN6VQUBppqkoBjut6gyi0aQ'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Qanday yordam kerak?")



@dp.message_handler()

async def echo(message: types.Message):
    try:
        lang = translator.detect(message.text)
        if len(message.text.split()) > 2:
            dest = 'uz' if lang == 'en' else 'uz'
            await message.reply(translator.translate(message.text, dest).text)
        else:
            if lang == 'en':
                word_id = message.text
            else:
                word_id = translator.translate(message.text, dest='en').text
            lookup = getDefinitions(word_id)
            if lookup:
                await message.reply(f"Word: {word_id} \nDefinitions: \n{lookup['definitions']}")
                if lookup.get('audio'):
                    await message.reply_audio(lookup['audio'])
            else:
                await message.reply("Bunday so'z topilmadi")
    except:
        await message.reply("Server error\n Contact:@beckzairov")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)