import os
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery)
from sample_config import Config as C

assistant = Client(
   "My-Assistant-Bot",
   api_id=C.APP_ID,
   api_hash=C.API_HASH,
   bot_token=C.TG_BOT_TOKEN,
)

IMAGE="""https://telegra.ph/file/e97f50bc4e0920f0c2475.jpg"""

START_TEXT="""👋Hᴇʟʟᴏ Tʜᴇʀᴇ {}!

🌹I'ᴍ Tʜᴇ Assɪsᴛᴀɴᴛ Oғ ƚԋҽɳυƙ ƈԋαɳυƙα.

🥰Aʟsᴏ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Hɪᴍ Usɪɴɢ Mᴇ..."""

HELP_TEXT="""☘️ <b><u>Hᴏᴡ Tᴏ Usᴇ Tʜεиᴜᴋ'ร Aรรɪรᴛᴀиᴛ</u> 

I'ᴍ A Assɪsᴛᴀɴᴛ Bᴏᴛ Oғ Tʜᴇɴᴜᴋ Cʜᴀɴᴜᴋᴀ. Hᴏᴡᴇᴠᴇʀ I'ᴍ Aʟsᴏ Wᴏʀᴋɪɴɢ As A PM Bᴏᴛ</b>...

<b><u>𝙼𝚊𝚒𝚗 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜</u></b> 

/start ⇝ <b>Tᴏ Sᴛᴀʀᴛ Mᴇ</b>
/help ⇝ <b>Tᴏ Gᴇᴛ Tʜɪs Mᴇssᴀɢᴇ</b>
/about ⇝ <b>Tᴏ Sᴇᴇ Mʏ Aʙᴏᴜᴛ Iɴғᴏ</b>"""

ABOUT_MSG="""🌷<b><u>A Pʀᴏᴊᴇᴄᴛ Bʏ ƚԋҽɳυƙ ƈԋαɳυƙα...</u></b>🌷

🙋‍♂I ᴀᴍ A Sᴄʜᴏᴏʟ Sᴛᴜᴅᴇɴᴛ Lᴇᴀʀɴɪɴɢ Iɴ Gʀᴀᴅᴇ 10😎. I'ᴍ Gᴏɪɴɢ Tᴏ Nᴀʀᴀɴᴅᴇɴɪʏᴀ Cᴇɴᴛʀᴀʟ Cᴏʟʟᴇɢᴇ. 🌹I Lɪᴠᴇ Iɴ Kᴀᴍʙᴜʀᴜᴘɪᴛɪʏᴀ ɪɴ Mᴀᴛᴀʀᴀ Dɪsᴛʀɪᴄᴛ.

☘️<b><u>𝘴ꪮꪑꫀ ỉꪀᠻꪮꪑꪖᡶỉꪮꪀ𝘴 ꪖ᥇ꪮꪊᡶ ꪑꫀ...</u></b>☘️

╔<b>Rᴇᴀʟ Nᴀᴍᴇ</b> » Tʜᴇɴᴜᴋ Cʜᴀɴᴜᴋᴀ
╠<b>Nɪᴋᴇ Nᴀᴍᴇ</b> » ঔ৫⃟➤Ꮋ‌ᵁ‌ᴺ‌᚜ᚸ⃝⃘⃟⃠‌᚛ᵀ‌ᴱ‌Ꮢ
╠<b>Lɪᴠᴇ ɪɴ</b>         » Kᴀᴍʙᴜʀᴜᴘɪᴛɪʏᴀ 
╠<b>Aɢᴇ</b>              » Yᴏᴜ Kɴᴏᴡ Iᴛ...
╚<b>Bɪʀᴛʜ Dᴀʏ</b>  » 2006 Sᴇᴘᴛᴇᴍʙᴇʀ 27"""

async def bot_msg():
    stat = f"""
🌹Thank You For Using My Assistant Bot.
"""
    return stat     

@assistant.on_callback_query(filters.regex("stats_call"))
async def stats_callbacc(_, CallbackQuery):
    text = await bot_msg()
    await assistant.answer_callback_query(CallbackQuery.id, text, show_alert=True)


@assistant.on_message(filters.command("start"))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('🙋‍♂️ 𝐇𝐞𝐥𝐩 🙋‍♂️', callback_data='help'),
        InlineKeyboardButton('🌹 𝐀𝐛𝐨𝐮𝐭 🌹', callback_data='about')
    ],
    [
        InlineKeyboardButton(◇────────────────◇", callback_data="stats_call")
    ],
    [   
        InlineKeyboardButton('🆘 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐇𝐞𝐥𝐩 🆘', url='http://t.me/Itzmedevinda')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await assistant.send_photo(
        chat_id=message.chat.id,
        photo=IMAGE,
        caption=START_TEXT.format(message.from_user.mention),
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
        caption=ABOUT_MSG,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           

                           
@assistant.on_callback_query()
async def button(assistant, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.edit_text()
        await help(assistant, update.message)
      elif "home" in cb_data:
        await update.message.edit_text()
        await home(assistant, update.message)
      elif "about" in cb_data:
        await update.message.edit_text()
        await about(assistant, update.message)

assistant.run()
