from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассказать о лучшей девушке')],
        [KeyboardButton(text='Показать коплименты'),KeyboardButton(text='Нажми сюда')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие'
)


catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='O Polishe', callback_data='pl_polisha')],
        [InlineKeyboardButton(text='O botе', callback_data='pl_bot')],
        [InlineKeyboardButton(text='Profil', url='https://t.me/polinochka_ca')],
        [InlineKeyboardButton(text='Profil sozdatelya', url='https://t.me/xarok228')]
    ]
)