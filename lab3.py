import math
import numpy as np
import curses

students = []
courses = []
marks = {}

def addStudent(s_id,s_name,s_dob):
    studentadding = {"id" : s_id, 
            "name" : s_name,
            "dob" : s_dob,
            "gpa" : 0}

    students.append(studentadding)


def addCourse(id, name, credits):
    courseadding = {"id" : id,
                    "name" : name,
                    "credits" : credits}

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
            marks[course_id][input_id] = math.floor(mark)
            print(f"Mark saved: {input_id} - {mark}")
        else:
            print("Student not exists")


def calcGPA(sid):
    s_marks = []
    c_credits = []
    for c in courses:
        c_id = c['id']
        if c_id in marks and sid in marks[c_id]:
            s_marks.append(marks[c_id][sid])
            c_credits.append(c['credits'])

        if (s_marks == []):
            return 0

        np_marks = np.array(s_marks)
        np_credits = np.array(c_credits)

        gpa = np.average(marks, weight = credits)

        for s in students:
            if s['id'] == sid:
                s['gpa'] = gpa
                break

        return gpa

def sortGPA():
    students.sort(key=lambda s: s.get('gpa', 0), reverse = True)




addCourse("A1","Optimization",3)
addCourse("ICT1","Python",4)
addCourse("MAT1","Probability",4)

addStudent("2510337","Hoang","26 Jan 2007")
addStudent("2510012","An","27 Oct 2007")
addStudent("2510123","Phong", "9 Mar 2007")




def main_menu(stdscr):
    curses.echo() 
    
    while True:
        stdscr.clear()
        menu = (
            "0. Exit\n"
            "1. List Courses\n"
            "2. List Students\n"
            "3. Marks of a course\n"
            "4. Edit marks\n\n"
            "Enter number to use function: "
        )
        stdscr.addstr(0, 0, menu)
        
        choice = stdscr.getstr().decode('utf-8')
        stdscr.clear()
        
        if choice == '0':
            break
            
        elif choice == '1':
            stdscr.addstr(0, 0, f"Courses: {courses}")
            
        elif choice == '2':
            stdscr.addstr(0, 0, f"Students: {students}")
            
        elif choice == '3':
            stdscr.addstr(0, 0, "Enter course ID: ")
            c_id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(2, 0, f"Marks: {marks.get(c_id, 'No data')}")
            
        elif choice == '4':
            stdscr.addstr(0, 0, "Enter course ID: ")
            c_id = stdscr.getstr().decode('utf-8')
            
            if c_id not in marks:
                marks[c_id] = {}
                
            stdscr.addstr(1, 0, "Enter student ID: ")
            s_id = stdscr.getstr().decode('utf-8')
            
            stdscr.addstr(2, 0, "Enter mark: ")
            try:
                mark = float(stdscr.getstr().decode('utf-8'))
                marks[c_id][s_id] = math.floor(mark * 10) / 10
                stdscr.addstr(4, 0, f"Mark saved: {s_id} - {marks[c_id][s_id]}")
            except ValueError:
                stdscr.addstr(4, 0, "Invalid input!")

        if choice != '0':
            stdscr.addstr(6, 0, "Press Enter to continue...")
            stdscr.getstr()

curses.wrapper(main_menu)