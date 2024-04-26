from cryptography.fernet import Fernet

'''
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = loadKey()
fer = Fernet(key)

def view():
   with open('passwords.txt', 'r') as f:
       for line in f.readlines():
           data = line.rstrip()
           user, passw = data.split("|")
           print(f"User: {user} -- Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")


while True:
    mode  = input("Would you like to add or view existing password(s)? press q to quit. (view/add/q) : ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode!")
        continue