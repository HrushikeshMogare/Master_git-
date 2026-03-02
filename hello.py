print("Hello, World!")
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Login failed. Please try again.")

        