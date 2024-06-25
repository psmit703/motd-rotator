import json
from datetime import datetime as dt
import os
import random

birthMonth = 0  # 1-12, 0 if not applicable, set this to the month you were born to get a special message on your birthday
birthDay = 0  # 1-31, 0 if not applicable, set this to the day of the month you were born to get a special message on your birthday

messages = json.loads(open("motds.json", "r").read())

if dt.now().month == birthMonth and dt.now().day == birthDay:
    thisMessage = messages["birthday"]
elif dt.now().month == 6:
    thisMessage = messages["prideMonth"]
else:
    thisMessage = random.choice(messages["motds"])

os.system(f"""echo "{thisMessage}\n" > /etc/motd""")
