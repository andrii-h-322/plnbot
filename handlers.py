from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart, Command
import keyboards as kb
import random
from groq import Groq
from dotenv import load_dotenv
from photo_ids import PHOTO_IDS
import os
from datetime import date

load_dotenv()

user = Router()
vstr_date = date(2026, 1, 5)



@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Этот бот создан для одного особенного человека ',
        reply_markup=kb.menu
    )

@user.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Я обязательно помогу тебе')

@user.message(F.photo)
async def photo_handler(message: Message):
    await message.answer(f'Фото получено!\n\nЕго id: {message.photo[-1].file_id}')

@user.message(F.text == 'Рассказать о лучшей девушке')
async def cmd_hello(message: Message):
    await message.answer(
        'Привет Полиша! Я рад, что ты решила воспользоваться моими услугами!',
        reply_markup=kb.catalog
    )
#генерация комплимента от ИИ
async def get_ai_compliment() -> str:
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {
                'role': 'user',
                'content': 'Напиши один короткий и искренний комплимент девушке по имени Полина. Только сам комплимент, без предисловий. На русском языке. Называй ее нежно "Полиша".'
            }
        ]
    )
    return response.choices[0].message.content
#показать комплименты от ИИ
@user.message(F.text == 'Показать коплименты')
async def show_compliments(message: Message):
    await message.answer('Думаю... 💭')
    compliment = await get_ai_compliment()
    await message.answer(compliment + ' 💖')

#рандомное фото из папки photos
@user.message(F.text == 'Нажми сюда')
async def send_random_photo(message: Message):
    photo_id = random.choice(PHOTO_IDS)
    await message.answer_photo(photo=photo_id, caption='Одно из наших фото 😛 ')
#счетчик дней вместе
@user.message(F.text == 'Счетчик')
async def counter(message: Message):
    today = date.today()
    days_together = (today - vstr_date).days
    await message.answer(f'Мы вместе уже {days_together} дней! 💖')
#инфа о Полине
@user.callback_query(F.data == 'pl_polisha')
async def polisha_info(callback: CallbackQuery):
    today = date.today()
    days_together = (today - vstr_date).days
    await callback.answer(text='Информация о Полине!', show_alert=True)
    await callback.message.answer(
        text='Информация о Полине: \n\n Полина — девочка, которая: \n '
             '• смеётся над моими тупыми шутками уже ' + str(days_together) +
             ' дней подряд\n • заставляет меня улыбаться даже в самые хмурые дни\n '
             '• обладательница самых красивых глаз и самого доброго сердца в мире\n '
             '• делает лучшие тт в мире \n• пока не понимает, что я каждый день '
             'благодарю вселенную за то, что она именно такая\n '
             '• и заствляет биться мое сердце каждый раз, когда я вижу ее глаза'
    )
#инфа о боте
@user.callback_query(F.data == 'pl_bot')
async def bot_info(callback: CallbackQuery):
    await callback.answer(
        text='Бот создан в честь моей любимой девушки — самого лучшего человека в мире 💋 ',
        show_alert=True
    )
    await callback.message.answer(text='Информация о боте')

@user.callback_query(F.data == 'profil')
async def profil_info(callback: CallbackQuery):
    await callback.answer(text='Профиль Полиши!', show_alert=True)
    await callback.message.answer(text='Профиль Полиши')


