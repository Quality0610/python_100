string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

string = string.split()
length_list = []

for str in string:
    if ',' in str or '.' in str:
        str.
        length_list.append(len(str) - 1)
    else:
        length_list.append(len(str))

print(length_list)