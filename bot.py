import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from googletrans import Translator
from aiogram.dispatcher.filters import Text
from buttons import *
from sqlite_class import Database

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database()
translator = Translator()
admin = 5222507821

# create baza
db.create_table_users()

@dp.message_handler(commands=['start', 'help', 'restart'])
async def send_welcome(message: types.Message):
    global username
    global telegram_id
    username = message.from_user.username
    telegram_id = message.from_user.id
    data = db.select_users(telegram_id)
    if data is None:
        await message.reply("Send your phone number...", reply_markup=phone_number)
    else:
        await message.reply("You were registered!")
        await message.reply("I'm Google Translate Bot!\nSend text...")    
    
@dp.message_handler(content_types='contact')
async def send_welcome(message: types.Message):
    phone_number = message.contact["phone_number"]
    data = db.select_users(telegram_id)
    if data is None:
        db.insert_users(username, telegram_id, phone_number)
        await bot.send_message(admin, f"New user from @google_translate0_bot\n\nUsername: @{username}\nID: {telegram_id}")
        await message.answer("You are successfully registered!")
        await message.reply("Hi\nI'm Google Translate Bot!\nSend text...")
    else:
        await message.reply("You were registered!")
        await message.reply("I'm Google Translate Bot!\nSend text...")

@dp.message_handler()
async def echo(message: types.Message):
    global input_word
    input_word = message.text
    markup = await translate_buttons()
    await message.answer("Choose language...", reply_markup=markup)

@dp.callback_query_handler(Text(startswith='language_'))
async def echo(call: types.CallbackQuery):
    index = call.data.index('_')
    lang = call.data[index+1:]
    translation = translator.translate(input_word, dest=lang)
    await call.message.answer(translation.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)