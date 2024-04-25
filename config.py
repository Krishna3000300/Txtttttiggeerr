import os

API_ID = API_ID = 23989445

API_HASH = os.environ.get("API_HASH", "f9d8341dc5ad6978e623f34df457b6ed)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6633982389:AAG1KOupYsk8cwZEUmAO8jhzvia8ES9nXgg)

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6981453498))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


