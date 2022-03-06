import os
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery)
from sample_config import Config as C

assistant = Client(
   "My Assistant Bot",
   api_id=C.APP_ID,
   api_hash=C.API_HASH,
   bot_token=C.TG_BOT_TOKEN,
)

IMAGE="""https://telegra.ph/file/c7ff46a66f080b8e07a7c.jpg"""

START_TEXT="""Hᴇʟʟᴏ Tʜᴇʀᴇ 👋 {}!

🌹I'ᴍ Tʜᴇ Assɪsᴛᴀɴᴛ Oғ <b>ƚԋҽɳυƙ ƈԋαɳυƙα</b>...

🥰Aʟsᴏ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Hɪᴍ Usɪɴɢ Mᴇ..."""

HELP_TEXT="""☘️ Hᴏᴡ Tᴏ Usᴇ Tʜεиᴜᴋ'ร Aรรɪรᴛᴀиᴛ 

I'ᴍ A Assɪsᴛᴀɴᴛ Bᴏᴛ Oғ <b>Tʜᴇɴᴜᴋ Cʜᴀɴᴜᴋᴀ</b>. Hᴏᴡᴇᴠᴇʀ I'ᴍ Aʟsᴏ Wᴏʀᴋɪɴɢ As A PM Bᴏᴛ...

𝙼𝚊𝚒𝚗 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 

/start ⇝ <b>Tᴏ Sᴛᴀʀᴛ Mᴇ</b>
/help ⇝ <b>Tᴏ Gᴇᴛ Tʜɪs Mᴇssᴀɢᴇ</b>
/about ⇝ <b>Tᴏ Sᴇᴇ Mʏ Aʙᴏᴜᴛ Iɴғᴏ</b>"""

@assistant.on_message(filters.command("start"))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('🙋‍♂️ 𝐇𝐞𝐥𝐩 🙋‍♂️', callback_data='help'),
        InlineKeyboardButton('🌹 𝐀𝐛𝐨𝐮𝐭 🌹', callback_data='about')
    ],
    [   
        InlineKeyboardButton('🌻 𝐓𝐨𝐨𝐥𝐬 🌻', url='http://t.me/Itzmedevinda')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_photo(
        chat_id=message.chat.id,
        photo=IMAGE,
        caption=START_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           

@assistant.on_message(filters.command("help"))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🔙 𝐁𝐚𝐜𝐤', callback_data='home')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_photo(
        chat_id=message.chat.id,
        photo=IMAGE,
        caption=HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           

@assistant.on_message(filters.command("about"))
async def about(client, message):
  buttons = [[
        InlineKeyboardButton('🔙 𝐁𝐚𝐜𝐤', callback_data='home')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_photo(
        chat_id=message.chat.id,
        photo=IMAGE,
        caption="""About""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           

                           
@assistant.on_callback_query()
async def button(assistant, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(assistant, update.message)
      elif "home" in cb_data:
        await update.message.delete()
        await home(assistant, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(assistant, update.message)

assistant.run()
