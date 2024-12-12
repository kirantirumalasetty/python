#t = (1, 3, 5 , True, [10,30,50])
""" print(t)

print(type(t))

t1 = t[-1]
print(t1)

t[0] = 100  #'tuple' object does not support item assignment
print(t) """

""" print(dir(t))
#'count', 'index'

print(t.index(True))
print(t.count(1)) """

###UNpacking

t = (1,2)
# t1 = t[0]
# t2 = t[1]
t1,t2=t
print(t1, t2)