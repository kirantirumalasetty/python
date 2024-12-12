""" print("Hello world, this is my first python programm")
res = 10 + 20
print(res)
print(id(res))
print(type(res))

print("Addition of 10 and 20 is: ", res)
print("ID of the res is: ", id(res))
print("type of the res variable is: ", type(res))
 """
""" a = 10.23
b = 12.23
res = a + b
print(" addition of a and b is: ", res, "type of the res is : ",type(res))
 """
#str = "This is string"
#print(str, " & Type of the str is: ", type(str))
#print(dir(str))

""" 'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 
'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
'islower', 'isnumeric', 'isprintable', 'isspace', 
'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill' """
""" print(str.casefold())
print(str.istitle())
print(str.isdecimal())
print(str.encode())
print(str.capitalize())
print(str.casefold())
print(str.lower())
print(str.swapcase())
print(str.upper()) """

""" str = "Hello Kiran"
print(str.split(' '))
print(str.find('K'))
# str = str[2]
# print(str)
print(len(str)) """
a = True
b = False

print(a and b)
print(a or b)

a = 2
b = 4
print(a + b)
print(b - a)
print(b / a)
print( a % b)
print(a // b)
print(a ** b)