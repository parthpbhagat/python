# singup page
users = {}

def signup():
    print("=== Signup Page ===")
    
    username = input("Choose a username: ")
    if username in users:
        print(" Username already exists. Try a different one.")
        return

    password = input("Choose a password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print(" Passwords do not match.")
        return
    users[username] = password
    print(f" Signup successful! You can now log in, {username}.")

signup()


# login page 

def login():
    print("=== Login Page ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"Login successful. Welcome, {username}!")
        home_page(username)
    else:
        print(" Invalid username or password.")

def home_page(username):
    print("=== Home Page ===")
    print(f"Hello, {username}! You are now logged in.")
login()