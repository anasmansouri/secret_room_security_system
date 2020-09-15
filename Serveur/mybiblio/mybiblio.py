import time
from random import randint


def emulate_detection_of_a_person():
    path = "../drivers/mouvement_detection_sensor/pir"
    put_the_output_high(path)


def put_the_output_high(path_to_file):
    write_value_in_file(path_to_file, 1)


def put_the_output_low(path_to_file):
    write_value_in_file(path_to_file, 0)


def write_value_in_file(path_to_file, value):
    f = open(path_to_file, "w")
    f.write("{}".format(value))
    f.close()


def read_the_content_of_file(path_to_file):
    f = open(path_to_file, "r")
    content = f.read()
    f.close()
    return content
