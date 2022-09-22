import pywhatkit
from datetime import datetime

# cell number with country code...
receiver = "" # e.g +27712345678

message = ""

def getTime():
    # getting device time...
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S").split(":")
    hours = current_time[0]
    mins = current_time[1]

    return hours, mins

# count number of messages sent
sent = 0

while(True):
    # can use time to schedule messages
    time = getTime()
    hours = int(time[0])
    mins = int(time[1]) 
    
    # instant messages, i.e no need to schedule...
    pywhatkit.sendwhatmsg_instantly(receiver, message, 12, tab_close=True)

    # scheduled messages...
    # Uncomment 
    # pywhatkit.sendwhatmsg(receiver, message, hours, mins, 12, True, 2)

    sent+= 1
    print(sent)
