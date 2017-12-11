import psutil
import requests
from win10toast import ToastNotifier

def system():
    global count
    count = 0
    toaster = ToastNotifier()
    while(True):
        battery_percent = psutil.sensors_battery().percent
        battery_plugged = psutil.sensors_battery().power_plugged
        if battery_percent > 97 and battery_plugged is True and count is 0:
            count = 1
            toaster.show_toast('Battery Notification',"Laptop Battery Charged", duration=10)
            requests.post("https://maker.ifttt.com/trigger/System/with/key/nlLVkjulk6dnLob3ii2lnwIbYw4bCVsJVn9jHQt3z8W",
                          data={'value1': "Laptop Charged"})

        elif battery_percent < 25 and battery_plugged is False and count is 0:
            count = 1
            toaster.show_toast('Battery Notification', "Battery Low", icon_path="low_battery.png", duration=10)
            requests.post("https://maker.ifttt.com/trigger/System/with/key/nlLVkjulk6dnLob3ii2lnwIbYw4bCVsJVn9jHQt3z8W",
                          data={'value1': "Laptop Low battery"})

        elif 97 > battery_percent > 25 and count is 1:
            count = 0

system()

