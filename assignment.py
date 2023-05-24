def password():
    username = (input("Enter user: "))
    pass_word =str(input("Enter password: "))
    confirm_password= str(input("Confirm password: "))
    if pass_word == confirm_password:
        print("Password confirmed")
    else:
        print("Invalid password")

    password()



password()
