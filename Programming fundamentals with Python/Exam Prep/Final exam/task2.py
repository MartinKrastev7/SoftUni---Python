import re

text = input()
pattern = r"[\@+\#+](?P<color>[a-z]{3,})[\@+\#+]\W+?\/+(?P<amount>[0-9]+)\/+"
result = re.finditer(pattern, text)

for match in result:
    print(f"You found {match.group('amount')} {match.group('color')} eggs!")

#([\@+\#+])(?P<color>[a-z]{3,})([\@+\#+])(\W+)*\/+(?P<amount>[0-9]+)\/+
#([\@+\#+])(?P<color>[a-z]{3,})([\@+\#+])([\W]*)\/+(?P<amount>[0-9]+)\/+
#([\@+\#+])(?P<color>[a-z]{3,})([\@+\#+])([\W]?)+\/+(?P<amount>[0-9]+)\/+