import re

string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
string = re.sub('[,\.]', '', string) 

string = string.split()
length_list = []

for str in string:
        length_list.append(len(str))

print(length_list)