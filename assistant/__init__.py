import aiohttp
import logging
from pyrogram import Client
from sample_config import Config
from telethon import TelegramClient


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

assistant = Client("pmbot", bot_token=Config.BOT_TOKEN, api_hash=Config.API_HASH, api_id=Config.APP_ID,)
tele = TelegramClient("telethon", Config.APP_ID, Config.API_HASH)
aiohttpsession = aiohttp.ClientSession()
