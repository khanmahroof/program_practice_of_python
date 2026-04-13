#country-capital lookup
name = {
    'india':'Delhi',
    'iran':'Tehran',
    'dubai':'Abu Dabi',
    'saudi':'Riyadh'
}
user = input("Enter the country name : ")
item = user.upper()
result = name.get(item)
if result:
    print(f"Your country {item} capital is {result}")
else:
    print(f"You entered {item} this country is invalid")

