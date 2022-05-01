def check_valid(passw):
    is_not_valid = False
    if not 6 <= len(passw) <= 10:
        is_not_valid = True
        print("Password must be between 6 and 10 characters")
    #if not passw.isdigit() and not passw.isalpha():
    if not passw.isalnum():
        is_not_valid = True
        print("Password must consist only of letters and digits")
    if len([x for x in passw if x.isdigit()]) < 2:
        is_not_valid = True
        print("Password must have at least 2 digits")

    if not is_not_valid:
        print("Password is valid")
    return


password = input()
check_valid(password)

