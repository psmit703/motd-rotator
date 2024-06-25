import json
from datetime import datetime as dt
import os
import random

messages = json.loads(open("motds.json", "r").read())

if dt.now().month == 6:
    thisMessage = messages["prideMonth"]
else:
    thisMessage = random.choice(messages["motds"])

os.system(f"""echo "{thisMessage}\n" > /etc/motd""")
