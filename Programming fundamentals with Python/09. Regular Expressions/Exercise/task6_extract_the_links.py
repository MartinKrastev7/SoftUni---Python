import re

while True:
    site = input()

    if not site:
        break

    pattern = r"(?P<subdomain>[www]{3}).(?P<domain>[A-Za-z0-9\-]+)(?P<extension>\.[a-z]+)+"
    result = re.finditer(pattern, site)

    for match in result:
        print(match.group())

