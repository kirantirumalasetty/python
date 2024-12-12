""" d = {'k': 123}
print(d['k'])

d= {'k': 123, 'k': 1234}
print(d['k'])

d = {'k': 123, (1, 2, 3, 4): 123}
print(d[(1, 2, 3, 4)]) """

""" d = {'k': 123, (1, 2, 3, 4): 123, (1,2,3,4,5): list(str(123))}
print(d[(1,2,3,4,5)])

print(dir(d))

#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

print(d.keys())
print(d.values())
print(d.items) """

# A dict isa mutable datatype
##set

""" s = {'a', 'a', 'b', 'c'}
print(s)

#s[0] = 'abc' #'set' object does not support item assignment
print(dir(s)) """
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
# 'isdisjoint', 
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

s = {"apple", "banana", "cherry"}
print("banana" in s)
print("kiran" in s)