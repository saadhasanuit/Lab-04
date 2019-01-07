print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 1")
# Solving Quadratic Equation
value_1 = eval(input("Please enter the value of a:"))
value_2 = eval(input("Please enter the value of b:"))
value_3 = eval(input("Please enter the value of c:"))
d = 2*value_1
if d ==0:
    print("Since the value of a is 0 the equation can not be solved further")
else:
    import math
    res_1=(-(value_2)+(math.sqrt(((value_2)**2)-(4*(value_1)*(value_3)))))/d
    res_2=(-(value_2)-(math.sqrt(((value_2)**2)-(4*(value_1)*(value_3)))))/d
    print("The two values are:",res_1,",",res_2)
