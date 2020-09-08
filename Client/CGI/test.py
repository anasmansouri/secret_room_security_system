#!/usr/bin/env python
import cgi
import cgitb
import sys
import subprocess
import sqlite3


def check_the_user_info(user_id, password):
    connection = sqlite3.connect("/www/room_management.db")
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM USERS"):
        if (str(row[0]) == user_id) and (str(row[1]) == password):
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
            print("<h2>user name is  {} est : </h2>".format(form["user_id"].value))
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
