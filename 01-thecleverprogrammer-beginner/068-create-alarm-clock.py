from datetime import datetime

import playsound

alarm_time = input('Enter alarm time - HH:MM:SS: \n')

alarm_hour, alarm_minutes, alarm_seconds = alarm_time[0:2], alarm_time[3:5], alarm_time[6:8]
print(alarm_hour, alarm_minutes, alarm_seconds)
print(datetime.now())

while True:
    now = datetime.now()

    current_hour = now.strftime('%H')
    current_minutes = now.strftime('%M')
    current_seconds = now.strftime('%S')

    if alarm_hour == current_hour and \
            alarm_minutes == current_minutes \
            and alarm_seconds == current_seconds:
        playsound.playsound('../resources/alarm.mp3')
        break
