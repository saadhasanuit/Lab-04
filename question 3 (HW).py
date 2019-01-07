print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 3")
# Checking whether the given string is Palindrome or not Palindrome
string = input("Please enter the word:")
string = string.casefold()
rev = reversed(string)
if list(string) == list(rev):
    print("This is a Palindrome")
else:
    print("This is a not a Palindrome")
