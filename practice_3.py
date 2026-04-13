# # #create a List from user input
# # user_list = []

# # for i in range (1,4):
# #    item = int(input(f"Enter the number {i} :"))
# #    user_list.append(item)
# # print(f"After creating your list is : {user_list} ")

# print(dir(list))

# """
# Functions available in list 


#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# """

# print(dir(tuple))
# print(dict)
# print(dir(set))


list1  = [x for x in range(100, 200, 10)] # list comprehension   100, 110, 120, 130 
print(list1)

for i in list1:
    print(i,end=' ')      # 100, 110,120  #this end syntax is use for removing the , and 

for i in range(len(list1)):
    print(list1[i],end=' * ') # leng    100, 1



dict1 = {x: 60*x for x in range(1,10)}
# print(dict1)

# for key, value in dict1.items():
#     print(f"{key}: {value}")
for key,value in dict1.items():
   temp = value
   dict1[key] = temp+5
print(dict1)



#Tuple

my_tuples = ('banana', 'mango', 'apple', 'orange')
for fruits in my_tuples:
   print(fruits)



#set

my_set = {'banana', 'mango', 'apple', 'orange'}
for fruits in my_set:
   print(fruits)



#string

item = 'python'
for char in item :
   print(char)