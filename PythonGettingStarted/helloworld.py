print("hello world")
print("----------------------------------------")

#example of string interpolation
name = "Hello"
desc = "World"
print(f"string interpolation, name: {name} desc: {desc}")
print("----------------------------------------")

#example of basic list and for-loop
student_names = ["Michael", "Jessica", "Noah", "Emelia", "Estella", "Chris", "Christen", "Roger", "Ginny"]
for name in student_names:
    print("the name is: {0}".format(name))
print("----------------------------------------")

#example of range in a for-loop
x = 0
for index in range(20):
    x += 100
    print("x is {0}".format(x))
print("----------------------------------------")

# example of range as a list
y = range(10)
for index in y:
    print("y is {0}".format(index))
print("----------------------------------------")

#example of loop with if-else
for name in student_names:
    if name == "Noah":
        print("Found Noah!")
    else:
        print(f"current name is: {name}")
print("----------------------------------------")

#example of loop with break
for name in student_names:
    if name == "Noah":
        print("Found Noah!")
        break
    else:
        print(f"current name is: {name}")
print("----------------------------------------")

#example of loop with continue
for name in student_names:
    if name == "Noah":
        continue
    else:
        print(f"current name is: {name}")
print("----------------------------------------")

#example of a while loop
x = 0
while x < 10:
    print(f"while x < 10 currently x is {x}")
    x += 1
print("----------------------------------------")

#example of a dictionary
dict = { "Name":"Michael", "Grade":12, "Score":98 }
print("name: {0}".format(dict["Name"]))
print("grade: {0}".format(dict.get("Grade", "Unknown")))
print("badkey: {0}".format(dict.get("badkey", "Unknown")))
print("----------------------------------------")

#example of a list of dictionarys
all_students = [
    { "Name":"Michael", "Grade":12, "Score":97 },
    { "Name":"Jessica", "Grade":11, "Score":99 },
    { "Name":"Noah", "Grade":1, "Score":100 },
    { "Name":"Emie", "Grade":0, "Score":98 }
]
for student in all_students:
    display = ""
    for key in student.keys():
        display += "{0}:{1} ".format(key, student[key])
    print(display)
print("----------------------------------------")

#example of a try catch block
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
student.update()
try:
    last_name = student["last_name"]
    test = "name" + 3
except KeyError:
    print("key doesn't exist in dictionary")
except TypeError:
    print("you cant add those together!")
except Exception as error:
    print("Unknown Error")
    print(error)
print("exception was caught and code executed.")
print("----------------------------------------")


# example of a function
students = []

def get_students_titlecase_fe():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return  students_titlecase

def print_students_titlecase_fe():
    students_titlecase = get_students_titlecase_fe()
    print(students_titlecase)

def add_student_fe(name, student_id = 332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def var_args(name, *args):
    print(name)
    print(args)

def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs)

student_list_fe = get_students_titlecase_fe()
add_student_fe("Mark")
print(students)
var_args("michael", "loves python", None, "hello", True)
var_kwargs("michael", description="loves python", feedback=None, pl_subscriber=True)
print("----------------------------------------")

# adding students to our app, by getting input
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return  students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id = 332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

student_list = get_students_titlecase()
student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)
print_students_titlecase()
print("----------------------------------------")





