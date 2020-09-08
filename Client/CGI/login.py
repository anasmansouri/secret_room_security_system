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


def take_the_client_info():
    print(""""
    <h1>Type your info</h1>

    <form action="post">
      <label for="userId">user Id:</label>
      <input type="text" id="userId" name="userId"><br><br>
      <label for="pwd">password :</label>
      <input type="password" id="pwd" name="pwd"><br><br>
      <input type="submit" value="Submit">
    </form>

    """)


def process_data(form):
    if "userId" in form and "pwd" in form:
        print("<p> chihaja </p>")

    # if "submit" in form and "userId" in form:
    #    print("the user Id {} the password {}".format(form["userId"].value, form["pwd"].value))
    #    if form["userId"].value == "anas" and form["pwd"].value == "123456789":
    # deactivate_buzzer()
    #        print("<p>go to the welcome page</p>")
    # url ="https://www.facebook.com/"
    # print('    <meta http-equiv="refresh" content="0;url={} />'.format(url$
    #    else:
    #        print("<p> the password is wrong please try again </p>")
    #        print("the user Id {} the password {}".format(form["userId"].value, form["pwd"].value))


cgitb.enable()
form = cgi.FieldStorage()

take_the_client_info()
process_data(form)

print(""""
</body>
</html>""")
