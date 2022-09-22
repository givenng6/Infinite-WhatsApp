from email import message
import pywhatkit
from datetime import datetime


receiver = ""; # cell number with country code...
message = ""

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S").split(":")
    hours = current_time[0]
    mins = current_time[1]

    return hours, mins

sent = 0

while(True):
    # can use time to schedule messages
    time = getTime()
    hours = int(time[0])
    mins = int(time[1]) 
    
    pywhatkit.sendwhatmsg_instantly(receiver, message, 12, tab_close=True)
    sent+= 1

    print(sent)
