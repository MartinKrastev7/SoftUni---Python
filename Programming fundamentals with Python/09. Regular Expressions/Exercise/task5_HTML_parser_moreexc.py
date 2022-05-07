import re

inputs = input()
title_pattern = r"<title>([^<>]*)<\/title>"
result_title = re.findall(title_pattern, inputs)
result_title = "".join(result_title)
print(f"Title: {result_title}")

body_pattern = r'<body>.*<\/body>'
body = re.findall(body_pattern, inputs)
body = ''.join(body)

pattern = r">([^><]*)<"
content = re.findall(pattern, body)
content = ''.join(content)
content = content.replace('\\n', '')
print(f'Content: {content}')

