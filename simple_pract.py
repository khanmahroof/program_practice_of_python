# def user(name):
#     print(name)
# user("marff")
"""
def multi(a, b):
    
    return  a * b
    
print(multi(6, 9))


"""


"""
*args example
"""

# def abc(a,b,*c):
#     # for i in range(len(args)):
#     #     print(args[i])
#     print(a,b,c)

# abc(1,2,3,4,5)


"""

**kwargs:
"""


# def xyz(**hjk):
#     for key, value in hjk.items():
#         print(f"{key}: {value}")


# xyz(x="X", y= "Y", z="Z")


"""
Default args example:
"""

# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10,20)

"""
Lambda functions
"""

# Function without using lambda.

# def c1(x): 
#     return x*x*x   

# print(c1(7))

# # FUnction using lambda
# c2 = lambda x,y : x*y*x  
# print(c2(7,3)) 


# list1  = [x for x in range(100, 200, 10)] # list comprehension   100, 110, 120, 130 
# print(list1)

# for i in list1:
#      print(i,end=' ') 


tuple1 = (x for x in range(10,80,8))
print(tuple1)
for i in range (tuple1):
    print(i)


#print(dir(tuple)) #count, index
#print(dir(set))   #union, update
#print(dir(dict))  #clear, fromekey, get, items, keys, pop, popitem, setdefault, update,values
#print(dir(list))   #append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort