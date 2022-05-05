title = input()
content = input()
comments_list = []
while True:
    comments = input()
    if comments == "end of comments":
        break

    comments_list.append(comments)

print("<h1>")
print(f"\t {title}")
print("</h1>")
print("<article>")
print(f"\t {content}")
print("</article>")

for word in comments_list:
    print("<div>")
    print(f"\t {word}")
    print("</div>")