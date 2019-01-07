print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 7")
#creating two 2x2 matrix
x=[[1,2],[4,6]]
y=[[11,13],[17,19]]
#creating a result matrix for storing value
result=[[0 for i in range(2)]for i in range(2)]
#iterate through rows
for i in range(len(x)):
    #iterate throught the column of the matrix
    for j in range(len(y)):
        #iterate through the row of the matrix
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
print(result)
