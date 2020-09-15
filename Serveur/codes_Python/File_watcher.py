import time
from watchdog.observers import Observer
from application_handler import Handler


class PirSensorWatcher:
    # Set the file on watch
    watchDirectory = "/home/pi/secret_room_security_system/Serveur/drivers/mouvement_detection_sensor/pir"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()
