# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "25976580"))
	API_HASH = os.environ.get("API_HASH", "b5562ab77a96e49bc9dd78cc103c6333")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6526976127:AAGu93YqffCmkQJF0AufgFHGiBGjOqGkyjk")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Kasukabe_files_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002088637887"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5906143481"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://developervro:developerrapuka@cluster9.gcj9754.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002088637887")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002213410383")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "5906143481").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** VPS PRIVATE SERVER
│
├🔸 **Developer:** TOJI
│
├🔹 **Bot Support:** [Support Group](https://t.me/Kasukabe_team)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/moviez_cartoonz)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [TOJI](https://t.me/Kasukabe_team)
 
 I am Super noob Please Support My Hard Work.

Not Updated or ```@Kasukabe_team```
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
