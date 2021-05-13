from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith(".txt"):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination_TXT + "/" + filename
                os.rename(src, new_destination)
            if filename.endswith(".zip"):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination_ZIP + "/" + filename
                os.rename(src, new_destination)
            else:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)


folder_to_track = 'D:/Downloads/Temp'
folder_destination = 'D:/Downloads/Test/ZIP'
folder_destination_ZIP = 'D:/Downloads/Test/ZIP'
folder_destination_TXT = 'D:/Downloads/Test/TXT'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
