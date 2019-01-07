print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("LAB-04 -9-NOV-2018")
print("QUESTION-05")
# Program which takes inital and final values and print sum of all numbers
initial_value = eval(input("Enter the initial value for the range :"))
final_value = eval(input("Enter the final value for the range :"))
numbers = range(initial_value,final_value+1)
sum = 0
for value in numbers:
    sum = sum+value
print("The sum is", sum)
