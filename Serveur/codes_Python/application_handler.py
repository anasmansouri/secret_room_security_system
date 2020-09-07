# import time module, Observer, FileSystemEventHandler 
import time
from watchdog.events import FileSystemEventHandler
import subprocess


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':

            print("start system")
