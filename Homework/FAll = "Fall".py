FAll = "Fall"
WINT = "Winter"
SPRN = "Spring"
SUMR = "Summer"


class Course:

    def __init__(self, code, title):
        self.title = title
        self.code = code


class Course_offering:

    def __init__(self, course, quarter, section, cap, related_sections):
        """
        Creates a course offering for a specific course

        Input:
            course : Course object
            quarter : str from constants
            section : Section object
            cap : int , max number of students
            related_sessions : list of related section objects
        """
        self.course = course
        self.quarter = quarter
        self.section = section
        self.cap = cap
        self.related_sessions = related_sections
        self.teachers = []
        self.students = []
    
    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            print("Teacher already assigned to class")

    def add_student(self, student):
        if not self.is_full() and student not in self.students:
            self.students.append(student)
        else:
            print("Class is full, or the student is already in the class")

    def is_full(self):
        return len(self.students) >= self.cap
    

class Section:

    def __init__(self, course, time):
        self.course = course
        self.time = time


class Related_section:

    def __init__(self, section, cap, teachers):
        self.section = section
        self.cap = cap
        self.teachers = teachers


class Student:

    def __init__(self, id, first_name, last_name, prefered_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.prefered_name = prefered_name
        self.courses = []

    def add_course(self, course_off, priority):
        if not course_off.is_full():
            self.courses.append((course_off, priority))
            course_off.add_student(self)