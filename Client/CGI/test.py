#!/usr/bin/env python
import cgi
import cgitb
import sys
import subprocess


def command(cmd, path):
    temp = subprocess.Popen([cmd, path], stdout=subprocess.PIPE)
    output = str(temp.communicate())
    output = output.split("\n")
    output = output[0].split('\\')
    res = []
    i = 0
    print("<br>")
    for line in output:
        print("<br>{}".format(
            line.replace("(", "").replace("'", "").replace("None", "").replace(",", "").replace(")", "").replace("n",
                                                                                                                 "")))


def list_the_content_of_a_folder():
    print('<h1>type your info:</h1>')
    print('<form method = "post">')
    print('<br> <input type = "text" name = "user_id" placeholder ="user_id"/>')
    print('<br> <input type = "text" name = "password" placeholder ="password"/>')
    print(' <input type = "submit" name = "login" value = "login"/>')

    if "login" in form:
        if form["user_id"].value == "anas" and form["password"].value == "123456789":
            print("<h2>user name is  {} est : </h2>".format(form["user_id"].value))
            #command("ls", form["chemin"].value)


print("Content-type: text/html\n\n")
print("<body>")
cgitb.enable()
form = cgi.FieldStorage()
#write_in_a_file()
list_the_content_of_a_folder()
print("</form>")
print("</body>")
print("</html>")