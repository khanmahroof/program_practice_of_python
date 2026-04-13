#String Manipulation: Palindrome Checker
def is_palindrome (s):
    result = s[::-1]
    if s == result:
        print(f"The palindrome is {s} ")
    else:
        print(f"{s} its not a palindrome ")
s = input("Enter the string : ")
is_palindrome(s)


# Madam manndm
