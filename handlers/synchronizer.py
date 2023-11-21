# from aiogram import Router, types, Bot, F
# from aiogram.types import Message
# from aiogram.filters import Command





# router = Router()

# @router.message(F.from_user.id == operator_chat_id & F.text)
# async def repeat_all_messages_to_helper(message:Message, bot:Bot):
#     global helper

#     text_message = message.text
#     await bot.send_message(helper, text_message)

# @router.message(F.from_user.id == helper & F.text)
# async def repeat_all_messages_to_user(message:Message, bot:Bot):
#     global operator_chat_id

#     text_message = message.text
#     bot.send_message(operator_chat_id, text_message)

# @router.message(F.from_user.id == operator_chat_id & F.photo)
# async def repeat_all_messages_to_helper(message:Message, bot:Bot):
#     global helper

#     photo = message.photo[-1].file_id
#     text = message.caption
#     await bot.send_photo(chat_id=helper, photo=photo, caption= text)

# @router.message(F.from_user.id == helper & F.photo)
# async def repeat_all_messages_to_user(message:Message, bot:Bot):
#     global operator_chat_id

#     photo = message.photo[-1].file_id
#     text = message.caption
#     await bot.send_photo(chat_id=operator_chat_id, photo=photo, caption= text)
 
# @router.message(F.from_user.id == operator_chat_id & F.video)
# async def repeat_all_messages_to_helper(message:Message, bot:Bot):
#     global helper

#     video = message.video.file_id
#     text = message.caption
#     await bot.send_video(chat_id=helper, video=video, caption= text)

# @router.message(F.from_user.id == helper & F.video)
# async def repeat_all_messages_to_user(message:Message, bot:Bot):
#     global operator_chat_id

#     video = message.video.file_id
#     text = message.caption
#     await bot.send_video(chat_id=operator_chat_id, video=video, caption= text)
  
# @router.message(F.from_user.id == operator_chat_id & F.sticker)
# async def repeat_all_messages_to_helper(message:Message, bot:Bot):
#     global helper

#     sticker = message.sticker.file_id
#     await bot.send_video(chat_id=helper, sticker=sticker)

# @router.message(F.from_user.id == helper & F.stiker)
# async def repeat_all_messages_to_user(message:Message, bot:Bot):
#     global operator_chat_id

#     sticker = message.sticker.file_id
#     await bot.send_video(chat_id=operator_chat_id, sticker=sticker)