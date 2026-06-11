print("---Student Grade Calculator---")
subjects=int(input("Enter number of subjects: "))

total = 0
for i in range(subjects):
    marks=float(input(f"Enter marks of subject {i+1}: "))
    total+=marks
per= total / subjects

print("Total marks= ", total)
print("Percentage= ", per,"%")
# grading
if per >= 90:
    grade= "A"
elif per>= 80:
    grade="B"
elif per>= 70:
    grade="C"
elif per>= 60:
    grade="D"
else:
    grade= "F"
print("Grade: ", grade)
