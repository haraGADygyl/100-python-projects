dataset = {"ivan": "asdqwe", "dragan": "`123qwe"}

username = input("Enter your username: ")

if username in dataset:
    password = input("Enter your password: ")

    while password != dataset[username]:
        password = input("Enter your password again: ")
    print("Logged in")
else:
    print("Invalid username")
