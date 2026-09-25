students = []
courses = []
marks = {}

def addStudent(s_id,s_name,s_dob):
    studentadding = {"id" : s_id, 
            "name" : s_name,
            "dob" : s_dob}

    students.append(studentadding)


def addCourse(id, name):
    courseadding = {"id" : id,
                    "name" : name}

    courses.append(courseadding)

def input_marks(course_id):
    if course_id not in marks:
        marks[course_id]={}

    print(f"Entering marks of course {course_id}")
    print("Enter -1 to exit")
    while True:
        input_id = input("Enter student ID: ")

        if input_id == "-1":
            break

        exists = 0
        for s in students:
            if s['id'] == input_id:
                exists = 1
                s_name = s['name']
                break

        if exists == 1:
            mark = float(input("Enter mark: "))
            marks[course_id][input_id] = mark
            print(f"Mark saved: {input_id} - {mark}")
        else:
            print("Student not exists")

addCourse("A1","Optimization")
addCourse("ICT1","Python")
addCourse("MAT1","Probability")

addStudent("2510337","Hoang","26 Jan 2007")
addStudent("2510012","An","27 Oct 2007")
addStudent("2510123","Phong", "9 Mar 2007")

while True:
    print("0. Exit")
    print("1. List Courses")
    print("2. List Students")
    print("3. Marks of a course")
    print("4. Edit marks")
    usefunc = int(input("Enter number to use function: "))

    if usefunc == 1:
        print(courses)
    elif usefunc == 2:
        print(students)
    elif usefunc ==3:
        c_id = input("Enter course ID: ")
        print(marks.get(c_id,"No data"))
    elif usefunc == 4:
        c_id = input("Enter course ID: ")
        input_marks(c_id)
    else:
        break