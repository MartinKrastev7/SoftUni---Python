n = int(input())
usernames = set()

for _ in range(n):
    user_name = input()
    usernames.add(user_name)

for username in usernames:
    print(username)
