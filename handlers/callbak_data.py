import asyncio
import json
from aiogram import types
from misc import dp, bot
from .sqlit import change_status,cheak_black
import random


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1002102259287

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()

time_flag = 1


text_stop = """<b>Аяяй я смотрю, кто-то решил
пошалить 😏

Чтобы получить результат, нужно просмотреть все видео одно за другим. Сначала смотри видео, а потом нажимай🙏🙃</b>"""


@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    await bot.answer_callback_query(call.id)

    if call.data == 'go_7':
        await state.update_data(v2='stop')

        markup = types.InlineKeyboardMarkup()
        bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url = 'https://youtu.be/vGvXZGXZfVc')
        bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_8')
        markup.add(bat_a1)
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=52,reply_markup=markup)

        if time_flag == 1:
            await asyncio.sleep(240)  # (60 сек)

        await state.update_data(v2='start')






    if call.data == 'go_8':
        try:
            if ((await state.get_data())['v2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/RxabCCn18mk')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_9')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v3='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=54,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(240)  # (90 сек)
            await state.update_data(v3='start')


    if call.data == 'go_9':
        try:
            if ((await state.get_data())['v3']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🤓ПРОЙТИ ТЕСТ🤓', callback_data='go_test')
            markup.add(bat_a)
            #
            # await state.update_data(v4='stop')
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=56,reply_markup=markup)
            # if time_flag == 1:
            #     await asyncio.sleep(60)  # (90 сек)
            # await state.update_data(v4='start')

    if call.data == 'go_test':
        markup = types.InlineKeyboardMarkup()
        bat_a1 = types.InlineKeyboardButton(text='1️⃣', callback_data='go_10')
        bat_a2 = types.InlineKeyboardButton(text='2️⃣', callback_data='go_false')
        bat_a3 = types.InlineKeyboardButton(text='3️⃣', callback_data='go_false')
        markup.add(bat_a1, bat_a2, bat_a3)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=58, reply_markup=markup)

    if call.data == 'go_false':
        await call.message.answer("<b>Нет, это не Биткоин. Пересмотри видео выше и попробуй ещё раз🙃</b>")



    if call.data == 'go_10':
        markup = types.InlineKeyboardMarkup()
        bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/x8ZRbEVIR5E')
        bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_11')
        markup.add(bat_a1)
        markup.add(bat_a)

        await state.update_data(v5='stop')

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=60,reply_markup=markup)
        if time_flag == 1:
            await asyncio.sleep(120)  # (90 сек)
        await state.update_data(v5='start')


    if call.data == 'go_11':
        try:
            if ((await state.get_data())['v5']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/0bW2rjT4zHM')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_12')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v6='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=62,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(120)  # (90 сек)
            await state.update_data(v6='start')


    if call.data == 'go_12':
        try:
            if ((await state.get_data())['v6']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/NvgHMPmPZLI')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_13')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v7='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=64,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(360)  # (90 сек)
            await state.update_data(v7='start')



    if call.data == 'go_13':
        try:
            if ((await state.get_data())['v7']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/Z6C5mWnOsT4')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_14')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v8='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=66,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(420)  # (90 сек)
            await state.update_data(v8='start')

    if call.data == 'go_14':
        try:
            if ((await state.get_data())['v8']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/UGnzeq3Un4U')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_15')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v9='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=68,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(540)  # (90 сек)
            await state.update_data(v9='start')



    if call.data == 'go_15':
        try:
            if ((await state.get_data())['v9']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/Om_s-kULMNU')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_16')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v10='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=70,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(300)  # (90 сек)
            await state.update_data(v10='start')


    if call.data == 'go_16':
        try:
            if ((await state.get_data())['v10']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/jFxcOKypLtk')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_17')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v11='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=72,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(300)  # (90 сек)
            await state.update_data(v11='start')

    if call.data == 'go_17':
        try:
            if ((await state.get_data())['v11']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/i2bEhrUqWDA')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_18')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v12='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=74,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(120)  # (90 сек)
            await state.update_data(v12='start')

    if call.data == 'go_18':
        try:
            if ((await state.get_data())['v12']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/hvA9airqj1I')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_19')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v13='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=76,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(300)  # (90 сек)
            await state.update_data(v13='start')


    if call.data == 'go_19':
        try:
            if ((await state.get_data())['v13']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/YFs0_ptrWXI')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_20')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v14='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=78,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(120)  # (90 сек)
            await state.update_data(v14='start')


    if call.data == 'go_20':
        try:
            if ((await state.get_data())['v14']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/5ovUFD_Qlio')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_21')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v14='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=80,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(480)  # (90 сек)
            await state.update_data(v14='start')


    if call.data == 'go_21':
        try:
            if ((await state.get_data())['v15']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/5ovUFD_Qlio')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_22')
            markup.add(bat_a1)
            markup.add(bat_a)

            await state.update_data(v16='stop')

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=82,reply_markup=markup)
            if time_flag == 1:
                await asyncio.sleep(300)  # (90 сек)
            await state.update_data(v16='start')


    if call.data == 'go_22':
        try:
            if ((await state.get_data())['v16']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='👀СМОТРЕТЬ👀', url='https://youtu.be/oWd-T5FOm_k')
            bat_a = types.InlineKeyboardButton(text='🚀ДАЛЕЕ🚀', callback_data='go_23')
            markup.add(bat_a1)
            markup.add(bat_a)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=84,reply_markup=markup)



    if call.data == 'go_23':
        change_status(call.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        bat_a1 = types.InlineKeyboardButton(text='👥ЧАТ КОМАНДЫ👥', url='https://t.me/+ZLKzqIq7xuRhMjky')
        markup.add(bat_a1)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=86,reply_markup=markup)

        if time_flag == 1:
            await asyncio.sleep(86400)  # 24 часа

        NAME = call.message.chat.full_name


        text = f"""<b>👋 {NAME} 
У меня есть для тебя специальное предложение😉</b> 

Как видишь, я предоставляю действительно эффективные инструменты, но у меня еще недостаточно отзывов из-за недавнего старта обучения.

Итак, в чем заключается суть предложения: ты записываешь <b>видео-отзыв</b>, выражая свое мнение о курсе и уровне удовлетворенности покупкой, я в обмен <b>провожу видео-созвон</b>, где в течение <b>30 минут</b> отвечу на все вопросы по обучению.

<b>Шаги:</b> снимаешь видео-отзыв на телефон, отправляешь его мне в телеграм @king_vesting, после чего мы обговорим время и проведем видео-созвон.

<i><b>P.S. Прошу без лишних вопросов. Если интересно, отправьте видео-отзыв сразу, а если нет, то не нужно задавать вопросы по этой теме.</b></i>"""

        await bot.send_message(chat_id=call.message.chat.id, text = text, parse_mode='html')