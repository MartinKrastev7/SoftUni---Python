text = input().split("\\")

file_name = text[-1].split(".")[0]
file_extension = text[-1].split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")

#vtori nachin
def extract_file(data):
    needed_information = data[-1].split(".")
    file_name = needed_information[0]
    extension = needed_information[1]

    print(f"File name: {file_name}")
    print(extension)


d = input().split("\\")
extract_file(d)