names = input().split(", ")
sorted_list = sorted(names, key=lambda x: (-len(x), x))
print(sorted_list)

#vtori nachin
names = input().split(", ")
sorted_names = sorted(names) # po azbuchen red
sorted_names = sorted(sorted_names, key =lambda name: -len(name) ) # po duljina sortirane
whole_sorted_names = sorted(names, key=lambda name:(-len(name),name))#purvo po duljina, posle po azbuchen red