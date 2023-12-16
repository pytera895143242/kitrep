import random

from aiogram import types
from misc import dp, bot
import sqlite3

import asyncio

from aiogram.dispatcher import FSMContext
from .sqlit import info_members,add_black,cheak_black
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked, ChatNotFound

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID_3 = 941730379 #Джейсон
ADMIN_ID_4 = 678623761 # Бекир

ADMIN_ID_6 = 1079844264



ADMIN_ID =[ADMIN_ID_1,ADMIN_ID_2,ADMIN_ID_3,ADMIN_ID_4,750038359]
PASS_ID = [ADMIN_ID_1,ADMIN_ID_2,ADMIN_ID_3,ADMIN_ID_4,750038359]

channel = -1001987012532

passwd1 = random.randint(10000,100000)
passwd2 = random.randint(10000,100000)
passwd3 = random.randint(10000,100000)
passwd4 = random.randint(10000,100000)
passwd5 = random.randint(10000,100000)
passwd6 = random.randint(10000,100000)
passwd7 = random.randint(10000,100000)
passwd8 = random.randint(10000,100000)
passwd9 = random.randint(10000,100000)


passwd10 = random.randint(10000,100000)
passwd11 = random.randint(10000,100000)
passwd12 = random.randint(10000,100000)
passwd13 = random.randint(10000,100000)
passwd14 = random.randint(10000,100000)
passwd15 = random.randint(10000,100000)
passwd16 = random.randint(10000,100000)
passwd17 = random.randint(10000,100000)
passwd18 = random.randint(10000,100000)
passwd19 = random.randint(10000,100000)









def new_password1():
    global passwd1
    passwd1 = random.randint(10000,100000)

def new_password2():
    global passwd2
    passwd2 = random.randint(10000,100000)

def new_password3():
    global passwd3
    passwd3 = random.randint(10000,100000)

def new_password4():
    global passwd4
    passwd4 = random.randint(10000,100000)

def new_password5():
    global passwd5
    passwd5 = random.randint(10000,100000)

def new_password6():
    global passwd6
    passwd6 = random.randint(10000,100000)

def new_password7():
    global passwd7
    passwd7 = random.randint(10000,100000)

def new_password8():
    global passwd8
    passwd8 = random.randint(10000,100000)

def new_password9():
    global passwd9
    passwd9 = random.randint(10000,100000)



def new_password10():
    global passwd10
    passwd10 = random.randint(10000,100000)

def new_password11():
    global passwd11
    passwd11 = random.randint(10000, 100000)

def new_password12():
    global passwd12
    passwd12 = random.randint(10000,100000)

def new_password13():
    global passwd13
    passwd13 = random.randint(10000,100000)

def new_password14():
    global passwd14
    passwd14 = random.randint(10000,100000)

def new_password15():
    global passwd15
    passwd15 = random.randint(10000,100000)

def new_password16():
    global passwd16
    passwd16 = random.randint(10000,100000)

def new_password17():
    global passwd17
    passwd17 = random.randint(10000,100000)

def new_password18():
    global passwd18
    passwd18 = random.randint(10000,100000)

def new_password19():
    global passwd19
    passwd19 = random.randint(10000,100000)








class reg1(StatesGroup):
    name1 = State()
    fname1 = State()

class st_reg(StatesGroup):
    st_name = State()
    st_fname = State()
    step_q = State()
    step_regbutton = State()

class black_dodik(StatesGroup):
    name1 = State()
    fname1 = State()

@dp.message_handler(commands=['pass1'],state='*')
async def pass1_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd1}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}"
Получил пароль: {passwd1}"
Команда: pass1""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}"
Получил пароль: {passwd1}"
Команда: pass1""")


@dp.message_handler(commands=['pass2'],state='*')
async def pass2_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd2}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd2}
Команда: pass2""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd2}
Команда: pass2""")


@dp.message_handler(commands=['pass3'],state='*')
async def pass3_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd3}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd3}
Команда: pass3""")

        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd3}
Команда: pass3""")


@dp.message_handler(commands=['pass4'],state='*')
async def pass4_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd4}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd4}
Команда: pass4""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd4}
Команда: pass4""")


@dp.message_handler(commands=['pass5'],state='*')
async def pass5_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd5}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd5}
Команда: pass5""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd5}
Команда: pass5""")


@dp.message_handler(commands=['pass6'],state='*')
async def pass6_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd6}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd6}
Команда: pass6""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd6}
Команда: pass6""")



@dp.message_handler(commands=['pass7'],state='*')
async def pass7_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd7}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}"
ID: {message.from_user.id}
Получил пароль: {passwd7}
Команда: pass7""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd7}
Команда: pass7""")



@dp.message_handler(commands=['pass8'],state='*')
async def pass8_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd8}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd8}
Команда: pass8""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd8}
Команда: pass8""")

@dp.message_handler(commands=['pass9'],state='*')
async def pass9_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd9}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd9}
Команда: pass9""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd9}
Команда: pass9""")




@dp.message_handler(commands=['pass10'],state='*')
async def pass10_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd10}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}"
Получил пароль: {passwd10}"
Команда: pass10""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}"
Получил пароль: {passwd10}"


Команда: pass10""")




@dp.message_handler(commands=['pass11'],state='*')
async def pass11_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd11}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}"
Получил пароль: {passwd11}"
Команда: pass11""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}"
Получил пароль: {passwd11}"


Команда: pass11""")



@dp.message_handler(commands=['pass12'],state='*')
async def pass12_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd12}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd12}
Команда: pass12""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd12}
Команда: pass12""")


@dp.message_handler(commands=['pass13'],state='*')
async def pass13_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd13}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd13}
Команда: pass13""")

        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd13}
Команда: pass13""")


@dp.message_handler(commands=['pass14'],state='*')
async def pass14_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd14}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd14}
Команда: pass14""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd14}
Команда: pass14""")


@dp.message_handler(commands=['pass15'],state='*')
async def pass15_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd15}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd15}
Команда: pass15""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd15}
Команда: pass15""")


@dp.message_handler(commands=['pass16'],state='*')
async def pass16_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd16}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd16}
Команда: pass16""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd16}
Команда: pass16""")



@dp.message_handler(commands=['pass17'],state='*')
async def pass7_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd17}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}"
ID: {message.from_user.id}
Получил пароль: {passwd7}
Команда: pass17""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd17}
Команда: pass17""")



@dp.message_handler(commands=['pass18'],state='*')
async def pass18_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd18}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd18}
Команда: pass18""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd18}
Команда: pass18""")

@dp.message_handler(commands=['pass19'],state='*')
async def pass19_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in PASS_ID:
        await message.answer(text=f"Текущий пароль {passwd19}")

        try:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @{message.from_user.username}
ID: {message.from_user.id}
Получил пароль: {passwd19}
Команда: pass19""")
        except:
            await bot.send_message(chat_id= channel, text= f"""Администратор: @
ID: {message.from_user.id}
Получил пароль: {passwd19}
Команда: pass19""")




@dp.message_handler(commands=['admin'],state='*')
async def admin_ka(message: types.Message,state: FSMContext):
    await state.finish()
    id = message.from_user.id
    if id in ADMIN_ID:
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Трафик', callback_data='list_members')
        bat_c = types.InlineKeyboardButton(text='Рассылка', callback_data='write_message')
        bat_b = types.InlineKeyboardButton(text='Скачать базу', callback_data='baza')
        # bat_d = types.InlineKeyboardButton(text='Удаление ебланов', callback_data='black_user')

        markup.add(bat_a)
        markup.add(bat_c)
        markup.add(bat_b)
        # markup.add(bat_d)

        await bot.send_message(message.chat.id,'Выполнен вход в админ панель',reply_markup=markup)



@dp.callback_query_handler(text='black_user')  #УДАЛЕНИЕ ДОДИКОВ
async def delite_dodik(call: types.callback_query):
    if call.message.chat.id in ADMIN_ID:
        markap = types.InlineKeyboardMarkup()
        bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
        markap.add(bat0)
        await bot.send_message(text = 'Перешли сообщение от додика',chat_id=call.message.chat.id,reply_markup=markap)
        await black_dodik.name1.set()


@dp.message_handler(state=black_dodik.name1,content_types=['text','photo','video','video_note','voice']) # Предосмотр поста
async def redarkt_post(message: types.Message, state: FSMContext):
    try:
        user_id = message.forward_from.id
        add_black(user_id)
        await message.answer('Пользователь удалён 🩸')

    except Exception as e:
        await message.answer('У пидора закрытый аккаунт')



@dp.callback_query_handler(text='list_members')  # АДМИН КНОПКА ТРАФИКА
async def cheack_trafik(call: types.callback_query):
    if call.message.chat.id in ADMIN_ID:
        a = (info_members()) #КОЛИЧЕСТВО ВСЕХ ЧЕЛОВ
        await bot.send_message(call.message.chat.id, f'Количество пользователей: {a[0]}\n'
                                                     f'Финиширровало пользователей {a[1]}')

@dp.callback_query_handler(text='baza')
async def baza(call: types.callback_query):
    if call.message.chat.id in ADMIN_ID:
        a = open('server.db','rb')
        await bot.send_document(chat_id=call.message.chat.id, document=a)

########################  Рассылка  ################################


########################  Рассылка  ################################
@dp.callback_query_handler(text='write_message')  # АДМИН КНОПКА Рассылка пользователям
async def check(call: types.callback_query, state: FSMContext):
    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='Всей базе', callback_data='rasl_old')
    bat1 = types.InlineKeyboardButton(text='Дошли до конца', callback_data='rasl_all')
    bat2 = types.InlineKeyboardButton(text='Не дошли до конца', callback_data='rasl_finish')
    murkap.add(bat0)
    murkap.add(bat1)
    murkap.add(bat2)

    await bot.send_message(call.message.chat.id, 'Кому делаем рассылку?', reply_markup = murkap)
    await bot.answer_callback_query(call.id)



@dp.callback_query_handler(text_startswith='rasl_')  # АДМИН КНОПКА Рассылка пользователям
async def check(call: types.callback_query, state: FSMContext):
    if call.data == 'rasl_old':
        await state.update_data(rasl = 'rasl_old')
    elif call.data == 'rasl_all':
        await state.update_data(rasl = 'rasl_all')
    elif call.data[0:11] == 'rasl_groop_':
        await state.update_data(rasl = call.data[11:])
    elif call.data == 'rasl_finish':
        await state.update_data(rasl='rasl_finish')


    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    murkap.add(bat0)
    await bot.send_message(call.message.chat.id, 'Перешли мне уже готовый пост и я разошлю его всем юзерам',
                           reply_markup=murkap)
    await st_reg.step_q.set()
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text='otemena', state='*')
async def otmena_12(call: types.callback_query, state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Отменено')
    await state.finish()
    await bot.answer_callback_query(call.id)


@dp.message_handler(state=st_reg.step_q,content_types=['text', 'photo', 'video', 'video_note', 'voice'])  # Предосмотр поста
async def redarkt_post(message: types.Message, state: FSMContext):
    await st_reg.st_name.set()
    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    bat1 = types.InlineKeyboardButton(text='РАЗОСЛАТЬ', callback_data='send_ras')
    bat2 = types.InlineKeyboardButton(text='Добавить кнопки', callback_data='add_but')
    murkap.add(bat1)
    murkap.add(bat2)
    murkap.add(bat0)

    await message.copy_to(chat_id=message.chat.id)
    q = message
    await state.update_data(q=q)

    await bot.send_message(chat_id=message.chat.id, text='Пост сейчас выглядит так 👆', reply_markup=murkap)


# НАСТРОЙКА КНОПОК
@dp.callback_query_handler(text='add_but', state=st_reg.st_name)  # Добавление кнопок
async def addbutton(call: types.callback_query, state: FSMContext):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, text='Отправляй мне кнопки по принципу Controller Bot')
    await st_reg.step_regbutton.set()
    await bot.answer_callback_query(call.id)


@dp.message_handler(state=st_reg.step_regbutton, content_types=['text'])  # Текст кнопок в неформате
async def redarkt_button(message: types.Message, state: FSMContext):
    arr3 = message.text.split('\n')
    murkap = types.InlineKeyboardMarkup()  # Клавиатура с кнопками

    massiv_text = []
    massiv_url = []

    for but in arr3:
        new_but = but.split('-')
        massiv_text.append(new_but[0][:-1])
        massiv_url.append(new_but[1][1:])
        bat9 = types.InlineKeyboardButton(text=new_but[0][:-1], url=new_but[1][1:])
        murkap.add(bat9)

    try:
        data = await state.get_data()
        mess = data['q']  # ID сообщения для рассылки

        await bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=mess.message_id,
                               reply_markup=murkap)

        await state.update_data(text_but=massiv_text)  # Обновление Сета
        await state.update_data(url_but=massiv_url)  # Обновление Сета

        murkap2 = types.InlineKeyboardMarkup()  # Клавиатура - меню
        bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
        bat1 = types.InlineKeyboardButton(text='РАЗОСЛАТЬ', callback_data='send_ras')
        murkap2.add(bat1)
        murkap2.add(bat0)

        await bot.send_message(chat_id=message.chat.id, text='Теперь твой пост выглядит так☝', reply_markup=murkap2)


    except:
        await bot.send_message(chat_id=message.chat.id, text='Ошибка. Отменено')
        await state.finish()


# КОНЕЦ НАСТРОЙКИ КНОПОК


@dp.callback_query_handler(text='send_ras', state="*")  # Рассылка
async def fname_step(call: types.callback_query, state: FSMContext):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    data = await state.get_data()
    mess = data['q']  # Сообщения для рассылки
    rasl = data['rasl']  # Сообщения для рассылки

    murkap = types.InlineKeyboardMarkup()  # Клавиатура с кнопками
    try:  # Пытаемся добавить кнопки. Если их нету оставляем клаву пустой
        text_massiv = data['text_but']
        url_massiv = data['url_but']
        for t in text_massiv:
            for u in url_massiv:
                bat = types.InlineKeyboardButton(text=t, url=u)
                murkap.add(bat)
                break

    except:
        pass

    if rasl == 'rasl_old':
        db = sqlite3.connect('server.db') #Рассылка по всей базе
        sql = db.cursor()
        users = sql.execute("SELECT id FROM user_time").fetchall()

    elif rasl == 'rasl_all':
        db = sqlite3.connect('server.db')  # Рассылка по тем кто прошел прогрев
        sql = db.cursor()
        users = sql.execute("SELECT id FROM user_time WHERE finish_stat = '1'").fetchall()

    elif rasl == 'rasl_finish':
        db = sqlite3.connect('server.db')  # Рассылка по тем кто не прошел прогрев
        sql = db.cursor()
        users = sql.execute("SELECT id FROM user_time WHERE finish_stat = '0'").fetchall()


    await state.finish()
    bad = 0
    good = 0
    delit = 0
    await bot.send_message(call.message.chat.id,
                           f"<b>Всего пользователей: <code>{len(users)}</code></b>\n\n<b>Расслыка начата!</b>",
                           parse_mode="html")

    for i in users:
        await asyncio.sleep(0.03)
        try:
            await mess.copy_to(i[0], reply_markup=murkap)
            good += 1
        except (BotBlocked, ChatNotFound):
            try:
                #delite_user(i[0])
                delit += 1

            except:
                pass
        except:
            bad += 1


    await bot.send_message(
        call.message.chat.id,
        "<u>Рассылка окончена\n\n</u>"
        f"<b>Всего пользователей:</b> <code>{len(users)}</code>\n"
        f"<b>Отправлено:</b> <code>{good}</code>\n"
        f"<b>Удалено пользователей:</b> <code>{delit}</code>\n"
        f"<b>Произошло ошибок:</b> <code>{bad}</code>",
        parse_mode="html"
    )
    await bot.answer_callback_query(call.id)
#########################################################