from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            usr, pwrd = data.split("|")
            print(f"User: {usr}" +"|" +"Password: {pwrd}")

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    #append mode
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + str(fer.encrypt(password.encode())) + "\n")
        



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

