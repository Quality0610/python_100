
string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
string = string.split()

nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dictionary = {}

for i , word in enumerate(string):
    print(i)
    print(word) 

    if i + 1 in nums:
        dictionary[word[:1]] = i + 1
    else:
        dictionary[word[:2]] = i + 1

print(dictionary)