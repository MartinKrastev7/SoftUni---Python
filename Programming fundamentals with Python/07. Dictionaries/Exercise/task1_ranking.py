contests_dict = {}

while True:
    command = input()

    if command == "end of contests":
        break

    command = command.split(":")
    contests = command[0]
    password = command[1]

    if contests not in contests_dict.keys():
        contests_dict[contests] = password

ratings_dict = {}

while True:
    command2 = input()

    if command2 == "end of submissions":
        break

    command2 = command2.split("=>")
    contest = command2[0]
    password = command2[1]
    username = command2[2]
    points = int(command2[3])

    if contest in contests_dict and contests_dict[contest] == password:
        if username not in ratings_dict:
            ratings_dict[username] = {contest: points}
        else:
            if contest in ratings_dict[username]:
                if ratings_dict[username][contest] < points:
                    ratings_dict[username][contest] = points
            else:
                ratings_dict[username][contest] = points

ordered_ratings = {n: v for n, v in (sorted(ratings_dict.items()))}
for key, value in ordered_ratings.items():
    v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    ordered_ratings[key] = v

max_points = 0
best_candidate = ""

for key, value in ordered_ratings.items():
    current_points = 0
    for sk, sv in value.items():
        current_points += sv
    if current_points > max_points:
        max_points = current_points
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in ordered_ratings.items():
    print(key)
    for candidate, points in value.items():
        print(f"#  {candidate} -> {points}")

#vtori nachin
contest_data = input()
contests_dict = {}

while contest_data != "end of contests":
    (contest, password) = contest_data.split(":")
    contests_dict[contest] = password

    contest_data = input()

submission_data = input()
users_dict = {}


while submission_data != "end of submissions":
    (contest, password, user, points) = submission_data.split("=>")

    if contest in contests_dict.keys():
        if contests_dict[contest] == password:
            if user not in users_dict:
                users_dict[user] = {}

            if contest not in users_dict[user]:
                users_dict[user][contest] = int(points)
            else:
                if users_dict[user][contest] < int(points):
                    users_dict[user][contest] = int(points)

    submission_data = input()

best_user = ""
best_points = 0

for user in users_dict.keys():
    total_points = sum(users_dict[user].values())
    if total_points > best_points:
        best_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {best_points} points.")



print("Ranking:")
for user in sorted(users_dict.keys()):
    print(user)
    for contest, points in sorted(users_dict[user].items(), key=lambda cp: -cp[1]):
        print(f"#  {contest} -> {users_dict[user][contest]}")