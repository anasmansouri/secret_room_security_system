import subprocess


def function():
    out = subprocess.Popen(['sudo', './', '../drivers/mouvement_detection_sensor/read_pir_value'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()


function()