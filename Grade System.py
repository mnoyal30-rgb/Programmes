print(" Grade System App")
name = input("Enter your name : ")
mark = float(input("Enter your total markn(out of 100): "))
if mark >= 90:
 grade = "A+"
elif mark >= 80:
 grade = "A"
elif mark >= 70:
 grade = "B"
elif mark >= 60:
 grade = "C"
elif mark >= 50:
 grade = "D"
else:
   grade = "F (Fail)"
   
print("\nstudent Name",name)
print("student Grade",grade)
print("student Mark",mark)