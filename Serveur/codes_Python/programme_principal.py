import os
import sys
import time

sys.path.append("../mybiblio")
from mybiblio import write_value_in_file, read_the_content_of_file


#


def function():
    f = os.popen("../drivers/mouvement_detection_sensor/read_pir_value")
    sensor_value = f.read()
    if sensor_value == "1":
        print("person detected")
        write_value_in_file("./file", "1")
        time.sleep(30)
        if read_the_content_of_file("./file") == "1":
            os.popen("sudo ../codes_C/launch_buzzer 9000 7000")
            print("launch buzzer")
        else:
            print("your welcome in the secret room")


if __name__ == "__main__":
    function()
