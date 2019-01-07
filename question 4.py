print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("LAB-04 -9-NOV-2018")
print("QUESTION-04")
# Python program to display all the prime numbers within an interval
l_limit = int(input("Enter lower limit range: "))
u_limit = int(input("Enter upper limit range: "))
print("Prime numbers between",l_limit,"and",u_limit,"are:")
for number in range(l_limit,u_limit + 1):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            print(number)
