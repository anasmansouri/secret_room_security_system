import cgi

print("<!DOCTYPE html>")
print("<html>")
print("<body>")


def take_the_client_info(form):

    print("<h1>Type your info</h1>")
    print("<form method=\"post\">")
    print("<label for=\"userId\">User id:  </label>")
    print("<input type=\"text\" id=\"userId\" name=\"userId\"><br><br>")
    print("<label for=\"pwd\">Password:</label>")
    print("<input type=\"password\" id=\"pwd\" name=\"pwd\"> <br><br>")
    print("<input type=\"submit\" value=\"Submit\">")
    print("</form>")

    if "submit" in form :
        if form["userId"] == "anas" and form["pwd"] == "123456789":
            print("<p> stop buzzer <p>")
            print("go to the welcome page")
        else:
            print("<p> the password is wrong please try again <p>")

cgi.enable()
form = cgi.FieldStorage()
take_the_client_info(form)

print(""""
</body>
</html>""")
