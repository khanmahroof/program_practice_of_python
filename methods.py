#tuple methods

#index ()

item = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = item.index(8)
print(x) 


#count ()

items = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = items.count(5)
print(x)

#set methods

#add(), discard(), remove(), clear(), union(), update()
s = {'g', 'e', 'k', 's'} 
d = {'k', 'a', 'c', 'd', 's'}

# adding 's'
s.add('f')
print('Set after adding updating:', s)

#union()
print("after updating:",s.union(d))


# discard ()
s.discard('g')
print('\nSet after discard updating:', s)

#remove ()
s.remove('e')
print('\nSet after removing updating:', s)

#pop ()
print('\nPopped element', s.pop())
print('Set after updating:', s)

#clear ()
s.clear()
print('\nSet after updating:', s)

#dictionary metods

#get()

user = {"name": "Alice", "age": 25}
print(user.get("name"))        
print(user.get("city", "Banglore"))

#key()
print(user.keys())

#value
print(user.values()) 

#item()
for key, value in user.items():
    print(f"{key}: {value}")

#setdefault
print(user.setdefault("alice",True))

#pop
print(user.pop("age"))

#popitem()
print(user.popitem())

#clear
print(user.clear())
