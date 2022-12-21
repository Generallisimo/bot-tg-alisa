import asyncio
import logging
from atexit import register
from cgitb import text
from email import message

from click import command
from numpy import row_stack
from pandas import Interval
from pip import main
import config
import logging

from aiogram.utils.markdown import hide_link
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType



#log
logging.basicConfig(level=logging.INFO)

#init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


#кнопка 1 первого развития
# inl_btn1=InlineKeyboardButton('показать тарифы 👀', callback_data='button1')
inl_kb1=InlineKeyboardMarkup().add(InlineKeyboardButton('показать тарифы 👀', callback_data='button1'))



#кнопка 2 развития 
inl_btn2=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Неделю - 500 ₽', callback_data='button2'),
                                                InlineKeyboardButton(text='Месяц -  1000 ₽', callback_data='button3'),
                                                InlineKeyboardButton(text='Навсегда - 1500 ₽', callback_data='button4'))



#кнопка 3 развития
inl_btn5=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Я оплатил ✅', callback_data='button5'),
                                                InlineKeyboardButton(text='Отмена ◀️', callback_data='button6'))




#кнопка 4 развития
inl_btn7=InlineKeyboardMarkup().add(InlineKeyboardButton(text='Скинул!', callback_data='button7'))


CHAT_ID='5544649143'






#photo
photo1 = open('photo/1.jpg', 'rb')
photo2 = open('photo/2.jpg', 'rb')
photo3 = open('photo/3.jpg', 'rb')
photo4 = open('photo/4.jpg', 'rb')



# скриншот пользователя
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def send_to_admin(message: types.Message):
    await bot.send_photo(CHAT_ID, photo=message.photo[0].file_id)
    #  await message.answer(text='Все прошло успешно, малыш😏')
    await message.answer_photo(photo=open('photo/3.jpg', 'rb'), caption='Ура! Скорее переходи по ссылке ниже 🔗 После успешного подтверждения оплаты тебе будет открыт доступ в канал 😘\n \nВтупить в канал: https://t.me/+N7_Y1aDa3u0xMTY9' )



#start
@dp.message_handler(commands=["start"])
async def cmd_start(mess: types.Message):
    # await bot.send_photo(CHAT_ID, photo=message.photo[0].file_id, caption='dd')

    # await bot.send_photo(CHAT_ID, photo=message.photo[-1].file_id, caption=('Привет 👋 Меня зовут Алиса. Я блоггер - выкладываю свои горячие фото и видео 😛 Люблю показать своё тело на камеру и обожаю внимание к себе. Подниму твое настроение и не только 🍆\n\nЭтот бот поможет тебе оказаться в моем VIP- канале 🔞'), reply_markup=inl_kb1)
    await mess.answer_photo(photo=open('photo/1.jpg', 'rb'), caption='Привет 👋 Меня зовут Алиса. Я блоггер - выкладываю свои горячие фото и видео 😛 Люблю показать своё тело на камеру и обожаю внимание к себе. Подниму твое настроение и не только 🍆\n\nЭтот бот поможет тебе оказаться в моем VIP- канале 🔞', reply_markup=inl_kb1)
    # await mess.delete()





#Первое развитие
@dp.callback_query_handler(text='button1')
async def but_call(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo=open('photo/2.jpg', 'rb'), caption='Получи доступ к эклюзивным фото и виде со мной 🔥\nХочу подписаться на...', reply_markup=inl_btn2)
    # await callback.message.delete()
    # await callback.answer("GOOD", show_alert=True) чтобы выскачило объявление






#Второе развитие
@dp.callback_query_handler(text='button2')
async def but_call2(callback: types.CallbackQuery):
    await callback.message.answer('Чтобы продолжить оплатите 500 руб. по следующий реквизитам:\n💳 банковская карта: 0000 0000 0000 0000', reply_markup=inl_btn5)
    # await callback.message.delete()
    

@dp.callback_query_handler(text='button3')
async def but_call2(callback: types.CallbackQuery):
    await callback.message.answer('Чтобы продолжить оплатите 1000 руб. по следующий реквизитам:\n💳 банковская карта: 0000 0000 0000 0000', reply_markup=inl_btn5)
    # await callback.message.delete()



@dp.callback_query_handler(text='button4')
async def but_call2(callback: types.CallbackQuery):
    await callback.message.answer('Чтобы продолжить оплатите 1500 руб. по следующий реквизитам:\n💳 банковская карта: 0000 0000 0000 0000', reply_markup=inl_btn5)
    # await callback.message.delete()








#кнопка возврата
@dp.callback_query_handler(text='button6')
async def but_call(callback: types.CallbackQuery):
    # await bot.send_photo(chat_id=message.from_user.id, photo=open('photo/4.jpg', 'rb'), caption=('Получи доступ к эклюзивным фото и виде со мной 🔥\nХочу подписаться на...'), reply_markup=inl_btn2)
    await callback.message.answer_photo(photo=open('photo/4.jpg', 'rb'),caption='Получи доступ к эклюзивным фото и видео со мной 🔥\nХочу подписаться на...', reply_markup=inl_btn2 )
    # await callback.message.delete()








#оплата
@dp.callback_query_handler(text='button5')
async def but_call5(callback: types.CallbackQuery):
    await callback.message.answer(text='Ты почти у цели 🧾 Отправь скриншот перевода боту')
    
    # await callback.message.delete()
    # await callback.answer()




# #финиш
# @dp.callback_query_handler(text='button7')
# async def but_call6(callback: types.CallbackQuery):
#     await callback.message.answer_photo(photo=open('photo/3.jpg', 'rb'), caption='Ура! Скорее переходи по ссылке ниже 🔗 После успешного подтверждения оплаты тебе будет открыт доступ в канал 😘\n \nВтупить в канал: https://t.me/+N7_Y1aDa3u0xMTY9' )
#     # await callback.answer()





#на тупые сообщения
@dp.message_handler()
async def echomes(msg: types.Message):
    await bot.send_message(msg.from_id ,text='Малыш🙈 у меня только команда /start')










# способ запуска
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = False)

