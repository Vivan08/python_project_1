# Name - Vivan Sethi
# Roll No - 2501060035
# Course - BCA
# Semester - 1st
# Subject - Problem Solving with Python
# Assignment : Unit 1 mini project
# Title : student profile console app
#  Date -



#task 1
print("welcome to the student profile console :")
stu_name = str(input("enter the full name of the student :"))
Ro_no = int(input("enter the roll number of the student :"))
Program = str(input("enter the program of the student :"))
Uni = str(input("Enter the name of the university :"))
City = str(input("enter the city of the student :"))
Age = int(input("enter the age of the student :"))
Hobby = str(input("Enter the hobby of the student :"))


#task 2
num1 = int(input("enter a number :"))
num2 = int(input("enter a second number :"))
print("arthematic operators" "\n")
print("+ operator adds numbers (num1+num2):" , num1+num2)
print("- operator subtracts the numbers (num1-num2):", num1-num2)
print("* operator multiples the number (num1*num2):", num1*num2)
print("/ operator divides the number (num1/num2) :" , num1/num2)
print("% operator gives the remainder of the number :(num1%num2)" ,num1%num2)
print("** operator is used to give exponential powers to a number (num1**num2) :" , num1**num2)
print("// gives the division of the number without its remainder (num1//num2) :" , num1//num2)
print("\n")
print("assignment operators ""\n")
num1 += 2
print( "+= operator adds any number after the equalto sign to any number (num1+=2) :" , num1)
num2 -= 1
print("-= subtracts one from any number (num2-=1) :",num2)
print("= operator assigns value to a variable (a=24) ")
print("\n")
print("comparision operators")
print("> and < operator compares two values to find the larger and smaller number and returns True or False (num1>num2) :",num1>num2 )
print("<= and >= opertors find if one number is greater than the other number or is equal to it returns True or False (num2>=num1) :" ,num2>=num1 )
print("== operator checks if two numbersare equal to each other or not it returns True or False (num1==num2) :" , num1==num2)
print("\n")
print("Logical operators")
print("and operator checks two conditions if both the conditions are true it returns True else it returns False (num2>num1 and num1<num2) :",num2>num1 and num1<num2)
print("or operator checks two conditions if one of the conditions are true it returns True else it returns False (num2>num1 or num1<num2) :",num2>num1 or num1<num2)
print("not operator checks one conditions if the condition is true it returns true else it returns False (not num1>num2) :",not num1>num2  )
print("\n")
print("membership operators")
print("in and not in check if the number is in a list or tuple (num1 not in [1,2,3,4]) :" ,num1 not in [1,2,3,4])


#task 3
greet = "hello"
print(greet + stu_name)
print(f"number 1 is {num1} and number 2 is {num2}")
print("escape character" "\t" "tab")
print("escape character" "\n" "newline")


#task 4
text = "this is an exaapmle for string functions"

#upper converts all characters of a string to upper case 
print(text.upper())

#lower converts all characters of a string to lower case
print(text.lower())

#count calculates the number of a characters in a string  
print(text.count("a"))

#capatalize converts the first letter of each new line to an upper case letter
print(text.capitalize())

# replace replaces a letter in the string with another character
print(text.replace("a","b"))


#task 5
print("-------------------------------")
print("\t""STUDENT PROFILE SYSTEM")
print("-------------------------------")
print(f"Name : {stu_name} \n")
print(f"Roll NO : {Ro_no} \n")
print(f"Course : {Program}\n")
print(f"University : {Uni}\n")
print(f"City : {City}\n")
print(f"Age : {Age}\n")
print(f"Hobby : {Hobby} \n")
print("---------------------------------")
print("Welcome to python programming !")


#Task 6
choice = str(input("enter y if you want to save the profile and n if you don't want to save the profile :"))
if choice == "y" :
    with open("save.txt","w") as f :
        f.write(f"student name :{stu_name} \n roll number is : {Ro_no} \nprogram is {Program} \nUniversity : {Uni} \nCity is :{City} \nhobby is {Hobby}")
else :
    print("profile not saved")