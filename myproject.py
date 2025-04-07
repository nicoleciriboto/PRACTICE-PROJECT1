def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old")
    print()

happy_birthday("Nicole", 21)
happy_birthday("Mike", 33)

def add_numbers(n1,n2):
    result = n1 + n2
    return result

number1 = int(input("Enter first num: "))
number2 = int(input("Enter second num "))
result=add_numbers(number1, number2)
print("The sum is ", result)

#function to find average marks
def find_average_marks(marks):
    sum_of_marks= sum(marks)
    total_subjects=len(marks)
    average_marks= sum_of_marks/total_subjects
    return average_marks

#function to calculate the grade
def compute_grade(average_marks):
    if average_marks>=80:
        grade = 'A'
    elif average_marks>=60:
        grade= 'B'
    elif average_marks>=50:
        grade= 'C'
    else:
        grade='F'
    return grade

marks=[55, 65, 75, 80, 60]
average_marks= find_average_marks(marks)
print("Your average mark is:", average_marks)

grade= compute_grade(average_marks)
print("Your grade is:", grade)

def evenNums(num):
    print(num)
    if num==2:
        return num
    else:
        return evenNums(num-2)
    
evenNums(8)

def Fibonacci(idx):
    if idx<=1:
        return idx
    else:
        return Fibonacci(idx-1)+ Fibonacci(idx-2)
    
print(Fibonacci(8))

#to count descending
for x in reversed(range(1,11)):
    print(x)
print('HAPPY NEW YEAR')

name= input("Enter your name: ")

while name=="":
    print("You did mot enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

name = "Nicole"
age = 21
print(f"Hello {name}, you are {age} years old")

age = 18
if age <= 18:
    print("You are a minor")
