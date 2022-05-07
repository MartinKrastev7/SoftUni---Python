import re

email = input()
pattern = r"(^|(?<=\s))((?P<user>[A-Za-z0-9]+)([\.\-\_]?)([A-Za-z0-9]+))@([A-Za-z]+([\.\-\_][A-Za-z]+)+)(\b|(?=\s))"

result = re.finditer(pattern, email)

for match in result:
    print(match.group())

#vtori nachin
text = input()
user_pattern = r"( |^)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z0-9]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

pattern = rf"{user_pattern}@{host_pattern}"

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])

