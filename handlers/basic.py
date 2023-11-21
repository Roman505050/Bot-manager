from aiogram import Router, types, Bot, F
from aiogram.types import Message
from aiogram.filters import Command

import os
from dotenv import load_dotenv

load_dotenv()
admin = os.getenv('ADMIN')

router = Router()

current_operator = None
operator_chat_id = None
helper = int(admin)
users_with_requests = set()
support_queue = []

@router.message(Command('start'))
async def handle_start(message: Message, bot: Bot):
    await message.answer("Вітаємо вас! Дякуємо за звернення в онлайн чат банкінгу.\nДля з'єднання з менеджером Банку використовуйте команду /support")
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    await message.answer(f'Новий запуск бота!\n \nUsername: {first_name}  {last_name}\nUser ID: {user_id}')

@router.message(Command('support'))
async def handle_support_request(message: Message, bot: Bot):
    global current_operator, operator_chat_id, helper
    print(message.from_user.id)
    if message.from_user.id == helper:
        await message.answer("Ошибка. Менеджер не може використовувати дану команду.")
    elif message.from_user.id not in users_with_requests:
        users_with_requests.add(message.from_user.id)

        if current_operator is None:
            current_operator = message.from_user.id
            operator_chat_id = message.chat.id
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            user_id = message.from_user.id
            await bot.send_message(current_operator, "Ваш запит отриманий. Очікуйте, будь ласка, з'єднання з менеджером. Введіть /stopsupport, щоб завершити обслуговування.")
            await bot.send_message(helper, f'Нове звернення! Username:{first_name} {last_name}. User ID:{user_id}')
        else:
            support_queue.append(message.from_user.id)
            await message.answer("Ви в черзі на підтримку. Зачекайте, будь ласка.")
    else:
        await message.answer("Ви вже зробили запит на підтримку. Очікуйте обробки.")

@router.message(Command('stopsupport'))
async def handle_stop_support(message: Message, bot: Bot):
    global current_operator, operator_chat_id, helper

    if message.from_user.id == current_operator:
        current_operator = None
        operator_chat_id = None
        users_with_requests.clear()
        await message.answer("Обслуговування завершено Користувачем. Ваш запит оброблено.")
        await bot.send_message(helper, "Обслуговування завершено Користувачем. Запит оброблено.")
        if support_queue:
            next_user = support_queue.pop(0)
            current_operator = next_user
            operator_chat_id = message.chat.id
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            user_id = message.from_user.id
            await bot.send_message(helper, f'Нове звернення! Username:{first_name} {last_name}. User ID:{user_id}')
            await bot.send_message(current_operator, "Ваш запит отриманий. Очікуйте, будь ласка, з'єднання з менеджером. Введіть /stopsupport, щоб завершити обслуговування.")
    elif message.from_user.id == helper:
        await bot.send_message(current_operator, "Обслуговування завершено Менеджером. Ваш запит оброблено.")
        await bot.send_message(helper, "Обслуговування завершено Вами. Запит оброблено.")
        current_operator = None
        operator_chat_id = None
        users_with_requests.clear()
        if support_queue:
            next_user = support_queue.pop(0)
            current_operator = next_user
            operator_chat_id = message.chat.id
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            user_id = message.from_user.id
            await bot.send_message(helper, f'Нове звернення! Username:{first_name} {last_name}. User ID:{user_id}')
            await bot.send_message(current_operator, "Ваш запит отриманий. Очікуйте, будь ласка, з'єднання з менеджером. Введіть /stopsupport, щоб завершити обслуговування.")
    else:
        await message.answer("Ошибка. Ви не робили запиту на підтримку!")


# operator_chat_id = int(operator_chat_id)
# helper = int(helper)

@router.message(F.from_user.id == operator_chat_id  and F.text)
async def repeat_all_messages_to_helper(message:Message, bot:Bot):
    global helper

    text_message = message.text
    await bot.send_message(helper, text_message)

@router.message(F.from_user.id == helper and F.text)
async def repeat_all_messages_to_user(message:Message, bot:Bot):
    global operator_chat_id

    text_message = message.text
    bot.send_message(operator_chat_id, text_message)

@router.message(F.from_user.id == operator_chat_id and F.photo)
async def repeat_all_messages_to_helper(message:Message, bot:Bot):
    global helper

    photo = message.photo[-1].file_id
    text = message.caption
    await bot.send_photo(chat_id=helper, photo=photo, caption= text)

@router.message(F.from_user.id == helper and F.photo)
async def repeat_all_messages_to_user(message:Message, bot:Bot):
    global operator_chat_id

    photo = message.photo[-1].file_id
    text = message.caption
    await bot.send_photo(chat_id=operator_chat_id, photo=photo, caption= text)
 
@router.message(F.from_user.id == operator_chat_id and F.video)
async def repeat_all_messages_to_helper(message:Message, bot:Bot):
    global helper

    video = message.video.file_id
    text = message.caption
    await bot.send_video(chat_id=helper, video=video, caption= text)

@router.message(F.from_user.id == helper and F.video)
async def repeat_all_messages_to_user(message:Message, bot:Bot):
    global operator_chat_id

    video = message.video.file_id
    text = message.caption
    await bot.send_video(chat_id=operator_chat_id, video=video, caption= text)
  
@router.message(F.from_user.id == operator_chat_id and F.sticker)
async def repeat_all_messages_to_helper(message:Message, bot:Bot):
    global helper

    sticker = message.sticker.file_id
    await bot.send_sticker(chat_id=helper, sticker=sticker)

@router.message(F.from_user.id == helper and F.stiker)
async def repeat_all_messages_to_user(message:Message, bot:Bot):
    global operator_chat_id

    sticker = message.sticker.file_id
    await bot.send_sticker(chat_id=operator_chat_id, sticker=sticker)
  