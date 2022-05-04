exam_results_dict = {}
language_submission_dict = {}

while True:
    command = input()

    if command == "exam finished":
        print("Results:")
        for key, value in exam_results_dict.items():
            print(f"{key} | {value}")
        break

    command = command.split("-")
    if len(command) < 3:
        user_name = command[0]
        action = command[1]
        if action == "banned":
            exam_results_dict.pop(user_name)
    else:
        user_name = command[0]
        language = command[1]
        points = int(command[2])

        if user_name not in exam_results_dict.keys():
            exam_results_dict[user_name] = points
        else:
            current_grade = exam_results_dict[user_name]
            if points > current_grade:
                exam_results_dict[user_name] = points

        if language not in language_submission_dict.keys():
            language_submission_dict[language] = 1
        else:
            language_submission_dict[language] += 1

print("Submissions:")
for key, value in language_submission_dict.items():
    print(f"{key} - {value}")

#vtori nachin
results_data = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    if "banned" not in command:
        data = command.split("-")
        name = data[0]
        tech = data[1]
        result = int(data[2])

        if tech not in results_data:
            results_data[tech] = {name: result}
            submissions[tech] = 1
        else:
            if name not in results_data[tech]:
                results_data[tech][name] = result
                submissions[tech] += 1
            else:
                if result > results_data[tech][name]:
                    results_data[tech][name] = result
                    submissions[tech] += 1
                else:
                    submissions[tech] += 1

    elif "banned" in command:
        data = command.split("-")
        name = data[0]
        for key, values in results_data.items():
            if name in values:
                del results_data[key][name]

print("Results:")
for key, value in results_data.items():
    for v in value:
        print(f"{v} | {value[v]}")
print("Submissions:")
for key in submissions:
    print(f"{key} - {submissions[key]}")