#!/usr/bin/env python
import cgi
import cgitb
import sys
import subprocess
import sqlite3

sys.path.append("/home/pi/project_mansouri/secret_room_security_system/Serveur/mybiblio")
from mybiblio import write_value_in_file


def check_the_user_info(user_id, password):
    connection = sqlite3.connect("/www/room_management.db")
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM USERS"):
        if (str(row[0]) == user_id) and (str(row[1]) == password):
            cursor.execute("INSERT INTO HISTORY VALUES('{}',datetime('now'))".format(row[0]))
            connection.commit()
            return True
    return False


def take_user_info():
    print('<h1>type your info:</h1>')
    print('<form method = "post">')
    print('<br> <input type = "text" name = "user_id" placeholder ="user_id"/>')
    print('<br> <input type = "password" name = "password" placeholder ="password"/>')
    print(' <input type = "submit" name = "login" value = "login"/>')

    if "login" in form:
        if check_the_user_info(form["user_id"].value, form["password"].value):
            write_value_in_file("/home/pi/project_mansouri/secret_room_security_system/Serveur/codes_Python/file", "0")
         else:
            print("<p> the user name or the password is wrong </p>")


print("Content-type: text/html\n\n")
print("<body>")
cgitb.enable()
form = cgi.FieldStorage()
take_user_info()
print("</form>")
print("</body>")
print("</html>")
