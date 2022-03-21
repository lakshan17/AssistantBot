import os

from pyrogram import filters
from telegraph import upload_file

@Tgraph.on_message(filters.command("tm"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐦𝐞𝐝𝐢𝐚 𝐟𝐢𝐥𝐞!")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("`𝐍𝐨𝐭 𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝!`")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    message = await message.reply_text("𝐏𝐫𝐨𝐜𝐜𝐞𝐬𝐬𝐢𝐧𝐠...")
    await message.edit_text("𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠...")
    await message.edit_text("[▇▇░░░░░░░░] 20%")
    await message.edit_text("[▇▇▇▇░░░░░░] 40%")
    await message.edit_text("[▇▇▇▇▇▇░░░░] 60%")
    await message.edit_text("[▇▇▇▇▇▇▇▇░░] 80%")
    await message.edit_text("[▇▇▇▇▇▇▇▇▇▇] 100%")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.edit_text(message, text=document)
    else:
        await message.edit_text(
            f"
☘️𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐓𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡!

◇─────────────◇
❤️‍🔥𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐁𝐲 : @ThenukChanukaBOT 
🔗𝐔𝐑𝐋 : [Click Here](https://telegra.ph{response[0]}) 
⚡𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [྅𝐀𝐦ͭ𝐚ͪ𝐳ͤ𝐨𝐧 ͯ™ ๛](http://t.me/TheAmazonX)
◇─────────────◇",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

