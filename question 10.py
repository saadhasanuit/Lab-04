print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("LAB-04 -9-NOV-2018")
print("QUESTION-10")
# Program to construct the following pattern, using a nested for loop
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print("")
