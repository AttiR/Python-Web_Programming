from datetime import datetime
import os
import pdb


def debug_variable(name, value):
    now = datetime.now()
    time_info = now.strftime("Today  %d.%m.%Y , and time is %H:%M.")
    file = os.path.basename(__file__)
    value = str(info1)
    information = f'{time_info} file name is  {file} {name} {value}\n'

    with open("text_log.txt", "a") as text_log:
        text_log.write(information)



