points = 0
print("Welcome to the Quiz")
print()

ans=input("1. What does CPU stand for?\n")
if ans.lower()== "central processing unit":
    print("Correct!")
    points +=1
else:
    print("Wrong!!")

ans=input("2. Which data type is mutable?\n"
"A) tuple\n" 
"B) string\n" 
"C) list\n" 
"D) integer\n")
if ans.lower()== "list" or "c":
    print("Correct!")
    points +=1
else:
    print("Wrong!!")

ans=input("3. Which keyword is used to create a function in python?\n" 
"A) function\n" 
"B) define\n" 
"C) fun\n" 
"D) def\n")
if ans.lower()== "def" or "d":
    print("Correct!")
    points +=1
else:
    print("Wrong!!")

ans=input("4. What does RAN stand for?\n")
if ans.lower()=="random access memory":
    print("Correct!")
    points +=1
else:
    print("Wrong!!")

ans=input("5. What is the purpose of a loop?\n" 
"A) store data\n" 
"B) repeat a block of code\n" 
"C) define variables\n" 
"D) create functions\n")
if ans.lower()== "repeat a block of code" or "b":
    print("Correct!")
    points +=1
else:
    print("Wrong!!")

print()
print("Quiz is completed")
print("Your score is", points,"out of 5")
