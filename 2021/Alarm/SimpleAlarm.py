import time
import winsound
from win10toast import ToastNotifier


def timer( message, minutes):

  notificator = ToastNotifier()
  notificator.show_toast('Alarm',f"Alarm will go off in {minutes} minustes...", duration = 50)
  
  time.sleep(minutes * 60)

  # winsound.Beep(frequency=1000, duration=1000)
  notificator.show_toast(f'Alarm',message, duration = 50)

if __name__ == "__main__":
  message = "Post on Github!"
  minutes = 1
  timer(message, minutes)