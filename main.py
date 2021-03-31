"""
# ================ B O T   D A T A  ================ #
name: "TRAGALDABAS-alarms"
username: "tragaldabas_bot"

# ====== A U T H O R   I N F O R M A T I O N ======= #
@author: Miguel Cruces

    I am the owner of the bot:
    TRAGALDABAS-alarms (@tragaldabas_bot)
Created on Telegram.

    To change ownership, send me an email. If you
want me to answer you sooner rather than later,
write me at gmail.

Doubts, complaints, insults:
E-mails:
  - mcsquared.fz@gmail.com
  - miguel.cruces.fernandez@usc.es
# ================================================== #
"""

import time as tm
from datetime import datetime as datim
from datetime import timedelta as tdelta
import schedule

from bot_alarm import BotAlarm
from keys import bot_token, bot_group_id


def reset_and_check():
    # dir_path_mcru = "/home/mcruces/Documents/Telegram_bot/test_data/"
    dir_path_trag = "/media/Datos2TB/tragaldabas/data/done/"

    bot_alarm = BotAlarm(
        bot_tkn=bot_token,
        bot_cht_id=bot_group_id,
        dir2check=dir_path_trag,
        report_correct=False
    )

    bot_alarm.check_run_process()


schedule.every().hour.at(":50").do(reset_and_check)
# schedule.every().second.do(reset_and_check)


def main(print_status: bool = False):
    while True:
        schedule.run_pending()
        tm.sleep(5 * 60)  # Time in seconds
        # tm.sleep(1)

        # ==================================================================== #
        if print_status:
            now = datim.now()
            utc_now = datim.utcnow()
            tfile = utc_now - tdelta(minutes=23.5)
            print(f"Current time: {now.strftime('%Y, doy %j at %H:%M:%S')} => "
                  f"search {tfile.strftime('tr%y%j%Hmmss.hld (%H:%M:%S)')} file.")
            print("Detach screen but keep running: <Ctrl-a><Ctrl-d>\n")
        # ==================================================================== #


if __name__ == '__main__':
    main(print_status=True)

# TODO: print bash return: "ls -la | tail -5" (function)
