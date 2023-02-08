# strName = input('Enter a string: ')
strName="motivation010"

# print(len(strName))
# print('strName' + 'bye')
# print(strName * 10)
# print(strName[0])
# print(strName[ :3])
# print(strName[-3:])
# print(strName[ : : -1])
# print(strName[6])
# print(strName[1:-1])
# print(strName.upper())
# print(strName.replace('a','e'))

newStr = ""

for char in strName:
    
    if char.isalpha():
        newStr += " "
    else:
        newStr += char    
        
        
print(f"[{newStr}]")        