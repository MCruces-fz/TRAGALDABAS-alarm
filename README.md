# Strong alarm for TRAGALDABAS detector

When the system is not saving data in the corresponding directory for whatever reason, it is expected to receive a message to the Telegram bot called ***TRAGALDABAS-alarms*** (*@tragaldabas_bot*)

> ***Bot Information***
>
> > **name**: *"TRAGALDABAS-alarms"*
> >
> > **username**: *"tragaldabas_bot"*
> >
> > **bot_token**: `*****`
> >
> > **bot_chatID** = `*****`
> >
> > **bot_groupID** = `*****`

## How To:
This is a little documentation to us this bot

### Start using it:

First, you need to create a python file called `keys.py` (if it doesn't exist yet)
```bash
touch keys.py
```

Open this file with your favourite text editor and write your bot-token and your chat IDs like these
```python
# keys.py

bot_token      = "H3r31sy0urb0tT0k3Nwr1tt3n"
bot_id_chat_1  = "1123458"
bot_id_chat_2  = "3141592"
bot_id_group_1 = "1618033"
bot_id_group_2 = "2718281"
```

Edit the `main.py` file to get your desired output, and run it in a screen of your always-alive device
```bash
screen -S ALARM
python3 main.py
```

#### Note:
To get information about how to use screens, read its manual:
```bash
man screen
```

### Get information about our bot

To get information about our bot in a json file, write a script like this
```python
# Script or commandline

from bot_alarm import BotAlarm
from keys import bot_token

bot = BotAlarm(bot_tkn=bot_token)
update = bot.get_update()
print(update)

"""
If you prefer check the json pretty printed,
you can import the json library and do this
"""

import json

print(json.dumps(update, indent=1))


# The link of this documentation sent by Telegram message:
bot.send_documentation()
```




## Sources:
[How to create a Telegram Bot and send messages with Python](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)

[Sending messages with Telegram bot (To a Telegram Group)](https://dev.to/rizkyrajitha/get-notifications-with-telegram-bot-537l)
