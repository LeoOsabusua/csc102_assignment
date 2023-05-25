def password():
    global confirm_password
    global username
    username = (input("Enter username: "))
    pass_word =str(input("Enter password: "))
    confirm_password= str(input("Confirm password: "))
    if pass_word == confirm_password:
        print("Password confirmed")
    else:
        print("Invalid password")
        password()
password()

def login():
    login_username = (input("Enter username:"))
    login_password = (input("Enter password:"))
    if login_password == confirm_password:
        print("login confirmed")
    else:
        print("Invalid login password")

        login()

login()