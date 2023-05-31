from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# phone number button
phone_number = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("📞 Share your phone number!", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

# all languages
languages = {
    "Uzbek 🇺🇿" : 'uz',
    "English 🇺🇸" : 'en',
    "Korean 🇰🇷" : 'ko',
    "Russian 🇷🇺" : 'ru',
    "French 🇫🇷" : 'fr',
    "Arabic 🇦🇪" : 'ar',
    "Chinese 🇨🇳" : 'zh-cn',
    "German 🇩🇪" : 'de',
    "Italian 🇮🇹" : 'it',
    "Japanese 🇯🇵" : 'ja',
    "Kannada 🇨🇦" : 'kn',
    "Norwegian 🇳🇴" : 'no',
    "Portuguese 🇵🇹" : 'pt',
    "Spanish 🇪🇸" : 'es',
    "Turkish 🇹🇷" : 'tr'
}

# translate buttons
async def translate_buttons():
    button = InlineKeyboardMarkup(row_width=3)
    for i, j in languages.items():
        button.insert(InlineKeyboardButton(text=i, callback_data=f"language_{j}"))
    return button
    