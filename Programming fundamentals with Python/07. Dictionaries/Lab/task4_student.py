text = input()
courses = {}

while ":" in text:
    data = text.split(":")
    #(name, id, course) = text.split(":") #tuple ot tri elementa i moje bez dolnite 3
    name = data[0]
    id = data[1]
    course = data[2]


    if course not in courses.keys():
        courses[course] = {}

    courses[course][id] = name

    text = input()

text = text.replace("_", " ")

if text in courses:
    for id in courses[text]:  # moje i samo tova bez gorniq if
        print(f"{courses[text][id]} - {id}")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
