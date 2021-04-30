"""
             A P A C H E   L I C E N S E
                    ------------ 
              Version 2.0, January 2004

       Copyright 2021 Miguel Cruces Fernández

  Licensed under the Apache License, Version 2.0 (the 
"License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an 
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
either express or implied. See the License for the specific 
language governing permissions and limitations under the 
License.

           miguel.cruces.fernandez@usc.es
               mcsquared.fz@gmail.com
"""

import requests
from datetime import datetime as datim
from datetime import timedelta as tdelta
import os
import subprocess


class BotAlarm:
    def __init__(self, bot_tkn: str, bot_cht_id: str = None, dir2check: str = None, report_correct: bool = False):
        self.bot_token = bot_tkn
        self.bot_chatID = bot_cht_id

        self.report_correct = report_correct

        self.dir2check = dir2check

        self.utc_time = datim.utcnow()
        self.gz_time = datim.now()

    def send_text(self, bot_message: str):
        """
        This function sends the text passed as argument in bot_message to
        the bot defined as self.bot_chatID

        :param bot_message: String with the message to send
        :return response.json(): The request
        """
        if self.bot_chatID is None:
            raise Exception("You must specify some chat ID! \nRead instructions in README.md")

        send_text = f"https://api.telegram.org/bot{self.bot_token}/" \
                    f"sendMessage?chat_id={self.bot_chatID}" \
                    f"&parse_mode=Markdown&text={bot_message}"
        response = requests.get(send_text)
        return response.json()

    def get_update(self):
        url = f"https://api.telegram.org/bot{self.bot_token}/getUpdates"
        response = requests.get(url)
        return response.json()

    def send_documentation(self):
        self.send_text("Here is the documetation, "
                       "Scroll-down and read the README:\n"
                       "https://github.com/MCruces-fz/TRAGALDABAS-alarm")

    def report_wrong(self, date_segment: str):
        """
        Report Error Message

        :param date_segment: String with the format YYDOYHH (year,
            day of the year, hour)
        """
        if self.dir2check is None:
            raise Exception("To use this feature you must specify the "
                            "directory to check HLDs files when BotAlarm is instantiated.")
        n_show = 5
        command = f"ls -gG {self.dir2check} " + "| awk '{print $4, $5, $6, $7}' " + f"| tail -{n_show}"
        last_files = subprocess.check_output(command, shell=True).decode("UTF-8")
        my_message = f"The file starting with tr{date_segment} could " \
                     f"not be found. Maybe TRAGALDABAS is not working.\n" \
                     f"These are the {n_show} last stored files:\n{last_files}"
        self.send_text(my_message)

    def report_ok(self, date_segment: str):
        """
        Report Okay Message

        :param date_segment: String with the format YYDOYHH (year,
            day of the year, hour)
        """
        my_message = f"File starting with tr{date_segment} found, " \
                     f"so that TRAGALDABAS is working normally."
        self.send_text(my_message)

    def set_date_segment(self):
        """
        Creates the string segment for the current UTC date

        :return f"{year}{doy}{hour}": String with the format YYDOYHH
            (year, day of the year, hour)
        """
        minutes2save = 47  # 23.5  # Estimated time it takes to save each file
        time_file = self.utc_time - tdelta(minutes=minutes2save)
        year = time_file.strftime('%y')  # Year without century as a decimal number [00,99]
        doy = time_file.strftime('%j')  # Day of the year as a decimal number [001,366]
        hour = time_file.strftime("%H")  # Hour (24-hour clock) as a decimal number [00,23]
        return f"{year}{doy}{hour}"  # Date segment

    def do_report(self, found: bool, date_sg: str):
        """
        Sends the report message with errors or correct confirmation

        :param found: Boolean -> True: Correct; False: Error
        :param date_sg: Date segment YYDOYHH with current UTC time
        """
        # found, date_sg = self.check_run_process()
        if not found:
            self.report_wrong(date_sg)
        elif found:
            if self.report_correct:
                self.report_ok(date_sg)  # Just to check if it works fine
        else:
            self.send_text("Something strange is happening with BotAlarm.")

    def check_run_process(self):
        """
        Checks if it is all right with the acquisition
        """

        if self.dir2check is None:
            raise Exception("To use this feature you must specify the "
                            "directory to check HLDs files when BotAlarm is instantiated.")

        filenames = os.listdir(self.dir2check)

        date_sg = self.set_date_segment()
        found = None
        for filename in filenames:
            if filename.startswith(f"tr{date_sg}"):
                found = True
                break
            else:
                found = False
        self.do_report(found, date_sg)
