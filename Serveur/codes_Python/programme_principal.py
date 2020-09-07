import subprocess
import os
import sys

sys.path.append("../mybiblio")
from mybiblio import write_value_in_file

# write_value_in_file("./file", "adf")


def function():
    f = os.popen("../drivers/mouvement_detection_sensor/read_pir_value")
    sensor_value = f.read()
    if sensor_value == "1":
        print("person detected")
        # write 1 in file_pip
        # waite for 30 seconds
        # test if the content of the file is still 1
        # if yes  then lunch the buzzer
        # else do nothing


if __name__ == "__main__":

    function()
