username = input()
password = input()
current_password = ""

while current_password != password:
    current_password = input()

print(f"Welcome {username}!")

########## vtori nachin
while True:
    current_password = input()

    if current_password == password:
        break

print(f"Welcome {username}!")