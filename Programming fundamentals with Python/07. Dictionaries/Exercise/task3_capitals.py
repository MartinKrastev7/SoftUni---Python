country = input().split(", ")
capital = input().split(", ")

dictionary = dict(zip(country, capital))

for key, value in dictionary.items():
    print(f"{key} -> {value}")

#vtori nachin
def capitals():
    countries_data = input().split(", ")
    capitals_data = input().split(", ")
    result = dict(zip(countries_data, capitals_data))

    for key,value in result.items():
        print(f"{key} -> {value}")




capitals()