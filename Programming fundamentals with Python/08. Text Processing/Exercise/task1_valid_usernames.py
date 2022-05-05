user = input().split(", ")
valid_users = []
is_valid = False

for name in user:
    if 3 > len(name) or len(name) > 16:
        is_valid = False
        continue
    for ch in range(0, len(name)):
        symbols = name[ch]
        if not symbols.isalnum() and symbols != "-" and symbols != "_":
            is_valid = False
            break
        else:
            is_valid = True

    if is_valid:
        valid_users.append(name)

print("\n".join(valid_users))

#vtori nachin
import string
def valid_username(data):
    flag = 0
    expected_elements = string.digits + string.ascii_letters + "_" + "-"
    for name in data:
        flag = 0
        if 3 > len(name) or len(name) > 16:
            flag = 1
        elif len([x for x in name if x in expected_elements]) != len(name):
            flag = 1

        elif flag == 0:
            print(name)

d = input().split(", ")
valid_username(d)

#treti nachin
usernames = input().split(", ")

for username in usernames:
    condition = username.isalnum() or "_" in username or "-" in username
    if 3 <= len(username) <= 16 and condition:
        print(username)