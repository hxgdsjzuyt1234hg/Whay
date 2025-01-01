import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25461006"))
    API_HASH = os.environ.get("API_HASH", "be4d9b5dc42758bccb2087b071738359")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7599956697:AAFCkCFKC4XK7RKPygYfoeOiv1-9SmwfN5M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQGEgQ4AdO7h_d3vvQhtDb5bLGm6KLsA638lsM_Uz97bDK6pnDPnXP2AQZQ6Mb8vEZQJGwF_BNDjVmyu13JvkseIPdMFAgQRrJ3BitDPIhUG3k0CiDJOLemubAtB7jif0Vhj96vxtIXjSdrtothQ8mn0ILWuQyW2umw3zZP-Yy2A45k3_Go26bpJlrbmzk10KGPU2esz9Nn9-UECokWnf4raIpanejjAOTNl9dZoNHHerNhX6NueGsHs2RNHSOmeiz9CKC4yox6YJixBFrRwk1SlcZpLC_jHH_N9wbbesPOuFvXcku9zXxvwvK0zlSaOQZQkv0FHdTpD3UtkAJARJ7cjIlbQAAAAGqLuGNAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@GxgjgxjgxvBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
