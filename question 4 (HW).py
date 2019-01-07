print("Muhammad Saad Hasan 18B-117-CS Section:-A")
print("9-NOV-2018")
print("LAB-04")
print("PROGRAMMING EXERCISE")
print("Question 4")
# Program for marks
name = input("Please enter your name:")
f_name = input("Please enter your father name:")
roll_no = input("Please enter your Roll Number:")
calculus = float(input("Please enter your marks of Calculus:"))
eng = float(input("Please enter your marks of English:"))
pf = float(input("Please enter your marks of Programming Fundamentals:"))
ict = float(input("Please enter your marks of ICT:"))
isl = float(input("Please enter your marks of Islamiat:"))
be = float(input("Please enter your marks of Basic electronics:"))
total_marks = calculus+eng+pf+ict+isl+be
percentage = ((total_marks)*100)/600
print("\n\n\t\t\t\tReport Card")
print("Name : "+str(name))
print("Father Name : "+str(f_name))
print("Roll.No : "+str(roll_no))
print("Marks of Calculus: "+str(calculus)+ "\nMarks of English: "+str(eng)+ "\nMraks of Progamming Fundamentals: "+str(pf)+ "\nMarks of ICT: "+str(ict)+ "\nMarks of Islamiat : "+str(isl)+ "\nMarks of Basic Electronic : "+str(be))
print("The total obtanied marks are : "+str(total_marks)+ "!")
print("The percentage is :"+str(percentage)+ "% !")
if percentage > 90:
    print("Grade : A+")
elif 90 > percentage > 80:
    print("Grade : A")
elif 80 > percentage > 70:
    print("Grade : B")
elif 70 > percentage > 60:
    print("Grade : C")
elif 60 > percentage > 50:
    print("Grdae : D")
elif 50 > percentage > 40:
    print("Grade : E")
else :
    print("Grade : F")

    
    
