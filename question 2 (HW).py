print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 2")
# Solving Arithmetic sequence of n numbers
a=eval(input("Input the value of first term :"))
d=eval(input("Input the value of common difference :"))
nth=eval(input("Input the nth term :"))
#applying the nth term formula
x=a+((nth-1)*d)
print("The first value when n is " , nth , "=" ,x)
while True:
    question=input("Either input YES or NO :")
    if (question == "yes"):
        nth=eval(input("Input the nth term :"))
        x=a +((nth-1)*d)
        print("The second value when n is " , nth , "=" , x)
    else:
        break
