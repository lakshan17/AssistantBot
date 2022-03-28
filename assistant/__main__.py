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

ADMIN=C.OWNER_ID

IMAGE="""https://telegra.ph/file/e97f50bc4e0920f0c2475.jpg"""

START_TEXT="""<b>Hᴇʟʟᴏ Tʜᴇʀᴇ {}👋👋👋!

🌹I'ᴍ Tʜᴇ Assɪsᴛᴀɴᴛ Oғ ƚԋҽɳυƙ ƈԋαɳυƙα.

🥰Aʟsᴏ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Hɪᴍ Usɪɴɢ Mᴇ...</b>"""

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
╚<b>Bɪʀᴛʜ Dᴀʏ</b>  » 2006 Sᴇᴘᴛᴇᴍʙᴇʀ 27

🥰 <i>Ⲋⲣⲉⲥⲓⲇⳑ Ⲧⲏⲇⲛⲕ⳽</i>
       💥𝐌𝐞😎
       💥𝐫𝐨𝐨𝐭@𝐍𝐎𝐎𝐁
       💥𝐃𝐢𝐥𝐚𝐬𝐧𝐚 𝐋𝐢𝐭𝐡𝐦𝐚𝐧𝐭𝐡𝐚
       💥𝐒𝐢𝐭𝐡𝐢𝐣𝐚 𝐃𝐞𝐰𝐦𝐢𝐧𝐚
"""

DEV_MSG="""🌷<b><u>𝙰𝚕𝚕 𝙾𝚞𝚛 𝙶𝚛𝚘𝚞𝚙𝚜, 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜 𝚊𝚗𝚍 𝙱𝚘𝚝𝚜</b><u/>🌷

Tʜɪs Is Aʟʟ Oᴜʀ Gʀᴏᴜᴘs, Cʜᴀɴɴᴇʟs Aɴᴅ Bᴏᴛs

🌹<b><u>ɠɾσυρʂ αɳԃ ƈԋαɳɳҽʅʂ</u></b>

➨ <b>Tʜᴇ AᴍᴀᴢᴏɴX</b>
✅Tʜɪs Is A Mʏ 𝙲ʜᴀɴɴᴇʟ
➨ <b>Gʀᴀᴘʜɪᴄ Mᴏʙɪʟᴇ</b>
✅Yᴏᴜ Cᴀɴ Gᴇᴛ Fʀᴇᴇ Lᴏɢᴏs Iɴ Tʜɪs Cʜᴀɴɴᴇʟ
➨ <b>Mᴀғɪᴀ Gɪᴠᴇᴀᴡᴀʏs</b>
✅Yᴏᴜ Cᴀɴ Gᴇᴛ Pʀɪᴍɪᴜᴍ Aᴄᴄᴏᴜɴᴛs Fʀᴇᴇ Usɪɴɢ Tʜɪs Cʜᴀɴɴᴇʟ
➨ <b>Sɪɴʜᴀʟᴀ Sᴜʙ Cᴀʀᴛᴏᴏɴ</b>
✅Sɪɴʜᴀʟᴀ Sᴜʙ Cᴀʀᴛᴏᴏɴs Aʀᴇ Aᴠᴀɪʟᴀʙʟᴇ Oɴ Tʜɪs Cʜᴀɴɴᴇʟ
➨ <b>SL Nɪɴᴊᴀ Tᴇᴀᴍ</b>
✅Tʜɪs Is A Bᴏᴛs Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ

🌹<b><u>Ⴆσƚʂ</u></b>

➨ <b>ThenukChanukaBOT</b>
✅Mʏ Assɪsᴛᴀɴᴛ Bᴏᴛ Iɴ Tᴇʟᴇɢʀᴀᴍ"""

DEV_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("྅𝐀𝐦ͭ𝐚ͪ𝐳ͤ𝐨𝐧 ͯ™ ๛ | •[🇱🇰]•", url="https://t.me/+iXEvYZN6KHtjZTRl"),
                    InlineKeyboardButton("GRΔƤHƖC MƠƁƖԼЄ", url="https://t.me/+vvS3VAX6OtU1ZjNl")
                ],
                [
                    InlineKeyboardButton("𝗠𝗔𝗙𝗜𝗔 ゞ™ 𝗚𝗶𝘃𝗲𝗮𝘄𝗮𝘆𝘀", url="https://t.me/MafiaGiveaways"),
                    InlineKeyboardButton("𝙎𝙞𝙣𝙝𝙖𝙡𝙖 𝙎𝙪𝙗 𝘾𝙖𝙧𝙩𝙤𝙤𝙣", url="https://t.me/+grlgQSGuaiQ1OTQ1")
                ],
                [
                    InlineKeyboardButton("••[sʟ ɴɪɴᴊᴀ ᴛᴇᴀᴍ]••", url="https://t.me/SlNinjaTeam"),
                    InlineKeyboardButton("Tʜεиᴜᴋ'ร Aรรɪรᴛᴀиᴛ", url="http://t.me/ThenukChanukaBOT")
                ],
                [
                    InlineKeyboardButton("🔙 𝐆𝐨 𝐁𝐚𝐜𝐤 ", callback_data="startmenu")
                ]
            ]
        )

START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌹 𝐀𝐛𝐨𝐮𝐭 🌹", callback_data="aboutnu"),
                    InlineKeyboardButton("🙋‍♂ 𝐇𝐞𝐥𝐩 🙋‍♂", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton('◇───────────────◇', callback_data="stats_call"),
                ],
                [
                    InlineKeyboardButton('🆘 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐇𝐞𝐥𝐩 🆘', url='http://t.me/MrHunterAX')
                ],
            ]
        )


ABOUT_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🌻", callback_data="devmenu"),
                    InlineKeyboardButton("🌷 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 🌷", url="http://t.me/MrHunterAX")
                ],
                [
                    InlineKeyboardButton("🔙 𝐆𝐨 𝐁𝐚𝐜𝐤 ", callback_data="startmenu")
                ]
            ]
        )

HELP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌹 𝐀𝐛𝐨𝐮𝐭 🌹", callback_data="aboutnu"),
                    InlineKeyboardButton("🌻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🌻", callback_data="devmenu")
                ],
                [
                    InlineKeyboardButton("🔙 𝐆𝐨 𝐁𝐚𝐜𝐤 ", callback_data="startmenu")
                ]
            ]
        )


async def bot_msg():
    stat = f"""
🌹Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Usɪɴɢ Mʏ Assɪsᴛᴀɴᴛ Bᴏᴛ.
root@MrHunterAX
"""
    return stat     

@assistant.on_callback_query(filters.regex("stats_call"))
async def stats_callbacc(_, CallbackQuery):
    text = await bot_msg()
    await assistant.answer_callback_query(CallbackQuery.id, text, show_alert=True)


@assistant.on_message(filters.command("start"))
async def start(bot, update):
    await update.reply_photo(
                    photo= IMAGE,
                    caption= START_TEXT.format(update.from_user.mention),
                    reply_markup= START_BTN,
                )                      

@assistant.on_message(filters.command("help"))
async def help(bot, update):
    await update.reply_photo(
                    photo= IMAGE,
                    caption= HELP_TEXT,
                    reply_markup=HELP_BTN,
                ) 
@assistant.on_message(filters.command("about"))
async def about(bot, update):
    await update.reply_photo(
                    photo= IMAGE,
                    caption= ABOUT_MSG,
                    reply_markup=ABOUT_BTN,
                ) 

@assistant.on_message(filters.command("dev"))
async def dev(bot, update):
    await update.reply_photo(
                    photo= IMAGE,
                    caption= DEV_MSG,
                    reply_markup=DEV_BTN,
                ) 

@assistant.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )

@assistant.on_callback_query(filters.regex("help"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=HELP_BTN,
     disable_web_page_preview=True
    )

@assistant.on_callback_query(filters.regex("about"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_MSG,
        reply_markup=ABOUT_BTN,
     disable_web_page_preview=True
    )      

@assistant.on_callback_query(filters.regex("dev"))
async def devmenu(_, query: CallbackQuery):
    await query.edit_message_text(DEV_MSG,
        reply_markup=DEV_BTN,
     disable_web_page_preview=True
    )    


@assistant.on_message(filters.command('submit') & filters.private)
async def report(bot, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=ADMIN, text=f"<b>⭕️NEW MESSAGE⭕️\n \n🧿 Name: {update.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=ADMIN, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ Your Feedback Successfully Submitted to the Admins</b>")
        else:
             await message.reply_text("<b>Use this command as the reply of any Message to Report</b>")

                         
        
@assistant.on_message(filters.command('reply') & filters.private)
async def replyt(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    userid=int(message.text.replace("/reply"," "))
                                    await bot.send_message(chat_id=userid, text=f"<b>An Admin is responded to your feedback ✨</b>")
                                    await bot.copy_message(chat_id=userid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Your Reply Successfully Send to the User</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Reply</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                          
@assistant.on_message(filters.command('send') & filters.private)
async def send(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/send"," "))
                                    await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")

@assistant.on_message(filters.command('id') & filters.group)
async def id(bot, message):
    await message.reply_text(f"<b>➲ Chat ID:</b> <code>{message.chat.id}</code>")
    

@assistant.on_message(filters.command("mlogo"))
async def logomake(bot, update):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("📤Uploading...")
    text = message.text.split(None, 1)[1]
    img = Image.open("./assistant/resources/IMG_20220327_195646_429.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./assistant/resources/Flashing.ttf", 400)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="yellow")
    img.save("masklogo2.jpg")
    await message.reply_photo(
                photo=f"masklogo2.jpg",
                caption= f"All rights received to @MrHunterAX"
            )
    await m.delete()

             
assistant.run()
