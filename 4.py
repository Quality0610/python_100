string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

string = string.split()
length_list = []

for str in string:
    if ',' in str:        
        length_list.append(len(str) - str.count(','))
    elif '.' in str:
        length_list.append(len(str) - str.count('.'))
    else:
        length_list.append(len(str))

print(length_list)