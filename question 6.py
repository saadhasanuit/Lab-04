print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("LAB-04 -9-NOV-2018")
print("QUESTION-06")
# program which takes no.of rows and no. of columns and generates value of list
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col
print(multi_list)
