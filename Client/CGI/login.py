import cgi

print("<!DOCTYPE html>")
print("<html>")
print("<body>")


def take_the_client_info(form):
    print(""""
    <h1>Type your info</h1>

        <form method="post">
          <label for="userId">User id:  </label>
          <input type="text" id="userId" name="userId"><br><br>
          <label for="pwd">Password:</label>
          <input type="password" id="pwd" name="pwd"> <br><br>
          <input type="submit" value="Submit">
        </form>
    
    """)
    if "submit" in form and "userId" in form and "pwd" in form:
        if form["userId"] == "anas" and form["pwd"] == "123456789":
            print("<p> stop buzzer <p>")
            print("go to the welcome page")
        else:
            print("<p> the password is wrong please try again <p>")


form = cgi.FieldStorage()
take_the_client_info(form)

print(""""
</body>
</html>""")
