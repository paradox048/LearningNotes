master_pwd = input("What is the master password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            usr, pwrd = data.split("|")
            print(f"User: {usr}\nPassword: {pwrd}")

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    #append mode
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + password + "\n")
        



while True:
    mode = input ("Would you like to add a new password or view existing ones? (view, add)")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode detected!")
        continue

