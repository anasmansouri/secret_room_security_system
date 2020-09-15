import os
import sys
import time

sys.path.append("../mybiblio")
from mybiblio import write_value_in_file, read_the_content_of_file




def function():
    print("hadi f5ater")
    f = os.popen("sudo ../drivers/mouvement_detection_sensor/read_pir_value")
    sensor_value = f.read()
    print(sensor_value)
    if sensor_value == "1":
        print("person detected")
        write_value_in_file("/home/pi/project_mansouri/secret_room_security_system/Serveur/tunnel/controle_buzzer", "1")
        write_value_in_file("../drivers/mouvement_detection_sensor/pir", "0")
        time.sleep(10)
        if read_the_content_of_file("/home/pi/project_mansouri/secret_room_security_system/Serveur/tunnel/controle_buzzer") == "1":
            os.popen("sudo ../codes_C/launch_buzzer 160000000 70000000")
            print("launch buzzer")
        else:
            print("your welcome in the secret room")


if __name__ == "__main__":
    while True :
        time.sleep(5)
        function()

