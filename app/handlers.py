from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#Подключили кнопки
import app.keyboards as kb

#Мы создали роутер - он делает роль диспетчера
router = Router()

#Хендлер - обработчик входящих сообщений
#Декоратор для диспетчера
@router.message(CommandStart()) #Создали команду CommandStart - /start
async def cmd_start(message: Message):
    #Данная функция отвечает на сообщения пользователя
    await message.answer(f'Дароу, {message.from_user.first_name}', 
    #Сообщение может иметь только один markup - здесь у нас не асинхрон
                         reply_markup=kb.main) #просто сообщение после команды
    await message.reply(f'Дароу, {message.from_user.first_name}',
    #Тут асинхронные кнопки                  
                        reply_markup=await kb.inline_cars()) #ответ на сообщение пользователя

@router.message(Command('help')) #Создали команду Command - /help
async def cmd_start(message: Message):
    await message.answer('Тебе никто не поможет...')

#В F.text хранится простое сообщение без /
@router.message(F.text == 'Как дела?') #Создали команду Command - /help
async def cmd_start(message: Message):
    await message.answer('Могла быть и лучше')

#Можно так получать изображения 
@router.message(F.photo) #Создали команду Command - /help
async def cmd_start(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

#Зная ID, то можно из бота отправлять картинки пользователю
#Вместо ID можно использовать ссылку
@router.message(Command('get_FNS')) #Создали команду Command - /help
async def cmd_start(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMaZxAL6Y5dkLdJqyHgtjJ4cO9xstEAAmf7MRtMYoBIGupYZMut-ooBAAMCAAN5AAM2BA',
        caption='Фнс схема'
    )