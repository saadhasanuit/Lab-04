print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 6")
# Program which will add two square matrices
matrix_a= [[5,9], [13,17]]
matrix_b= [[21,25], [29,33]]
matrix_sum=[[0,0], [0,0]]
#sum
for i in range (len(matrix_a)):
    for j in range(len(matrix_a[0])): 
        matrix_sum[i][j] = matrix_a[i][j] + matrix_b[i][j]
        
for i in matrix_sum:
    print(i)
