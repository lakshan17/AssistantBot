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

START_TEXT="hii"

HELP_TEXT="hui"

@assistant.on_message(filters.command("start"))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('🙋‍♂️ 𝐇𝐞𝐥𝐩 🙋‍♂️', callback_data='help'),
        InlineKeyboardButton('🌹 𝐀𝐛𝐨𝐮𝐭 🌹', callback_data='about')
    ],
    [
        InlineKeyboardButton('◇──────────────◇', query.answer("𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐒𝐭𝐚𝐫𝐭 𝐌𝐲 𝐁𝐨𝐭🥰", show_alert=True))
    ],
    [   
        InlineKeyboardButton('🌻 𝐓𝐨𝐨𝐥𝐬 🌻', url='http://t.me/Itzmedevinda'),
        InlineKeyboardButton('♻ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ♻', url='http://t.me/ItsMeDevinda')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_message(
        chat_id=message.chat.id,
        text=START_TEXT
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           

@assistant.on_message(filters.command("help"))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🔙 𝐁𝐚𝐜𝐤', callback_data='home'
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_message(
        chat_id=message.chat.id,
        text=HELP_TEXT
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           

@assistant.on_message(filters.command("about"))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🔙 𝐁𝐚𝐜𝐤', callback_data='home'
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_message(
        chat_id=message.chat.id,
        text="""About"""
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
