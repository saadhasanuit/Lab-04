print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 5")
# Generating a table from initial value to final
row=1
initial=int(input("give the initial value: "))
final=int(input("give the final value: "))
#creating a multi dimension array for storing value
mylist=[[0 for col in range(final+1)]for row in range(row)] #creating a multi dimension array for storing value

for i in range(initial,final+1):
    for j in range(initial,final+1):
        mylist[0][j]=i*j
    print(mylist)
