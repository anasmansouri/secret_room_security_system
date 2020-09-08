import cgi
import cgitb
import sys

# sys.path.append("../../Serveur/mybiblio")
# from mybiblio import write_value_in_file

print("<!DOCTYPE html>")
print("<html>")
print("<body>")


# def deactivate_buzzer():
#    write_value_in_file("../../Serveur/codes_Python/file", "0")


def your_welcome_to_the_secret_room():
    print("<p>your welcome to the secret room</p>")


def take_the_client_info(form):
    print('<h1>Type your info</h1>')
    print('<form method = "post">')
    print('<label for="userId">User id:  </label>')
    print('<input type="text" id="userId" name="userId"><br><br>')
    print('<label for="pwd">Password:</label>')
    print('<input type="password" id="pwd" name="pwd"> <br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    if "submit" in form and "userId" in form:
        if form["userId"].value == "anas" and form["pwd"].value == "123456789":
            # deactivate_buzzer()
            print("<p>go to the welcome page</p>")
            # url ="https://www.facebook.com/"
            # print('    <meta http-equiv="refresh" content="0;url={} />'.format(url$
        else:
            print("<p> the password is wrong please try again </p>")
            print("the user Id {} the password {}".format(form["userId"].value, form["pw$"].value))


cgitb.enable()
form = cgi.FieldStorage()



take_the_client_info()

your_welcome_to_the_secret_room()
take_the_client_info(form)

print(""""
</body>
</html>""")
