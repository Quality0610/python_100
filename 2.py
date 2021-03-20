string1 = 'パトカー'
string2 = 'タクシー'
answer_string = ''

for str1, str2 in zip(string1, string2):
    answer_string = answer_string + str1 + str2
    

print(answer_string)