initial_string = input()
command = input()
new_pass = initial_string

while command != "Done":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "TakeOdd":
        curr_password = new_pass
        new_pass = ""
        for i in range(len(curr_password)):
            if i % 2 != 0:
                new_pass += curr_password[i]
        print(new_pass)

    elif current_command == "Cut":
        index = int(command[1])
        length = int(command[2])

        substring = new_pass[index:index + length]
        if substring in new_pass:
            new_pass = new_pass.replace(substring, "", 1)
        print(new_pass)

    elif current_command == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in new_pass:
            new_pass = new_pass.replace(substring, substitute)
            print(new_pass)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {new_pass}")

#За да заработи както трябва да промениш следното

#1. Задаваш начална стойност на new_pass да е паролата от импут

#2. В случая за TakeOdd пазиш паролата досега. След това задаваш празна стойност на new_pass. Въртиш цикъла и взимаш символите от паролата досега като запазваш отново в new_pass

#Takes only the characters at odd indices and concatenates them together to
#obtain the NEW raw password and then prints it