import csv
import os
from abc import ABC, abstractmethod


# TASK 2: STUDENT CLASS, ENCAPSULATION AND ABSTRACTION


# Base class named Student. It inherits from ABC so that it
# can hold an abstract method (Requirement 4).
class Student(ABC):

    # REQUIREMENT 1: Store the student's ID, first name, last name,
    # programme and subject marks.
    # REQUIREMENT 2 (Encapsulation): The double underscore (__) makes
    # every attribute private so it cannot be changed directly.
    def __init__(self,StudentID,Fname,Lname,Programme,Math,English,Science):
        self.__StudentID=StudentID
        self.__Fname=Fname
        self.__Lname=Lname
        self.__Programme=Programme
        self.__Math=Math
        self.__English=English
        self.__Science=Science

    # REQUIREMENT 2 (Encapsulation): Getter methods for accessing
    # the private data.
    def get_StudentID(self):
        return self.__StudentID
    def get_Fname(self):
        return self.__Fname
    def get_Lname(self):
        return self.__Lname
    def get_Programme(self):
        return self.__Programme
    def get_Math(self):
        return self.__Math
    def get_English(self):
        return self.__English
    def get_Science(self):
        return self.__Science

    # REQUIREMENT 2 (Encapsulation): Setter methods for updating the
    # private data. The mark setters validate the value (0 to 100).
    def set_Programme(self,Programme):
        self.__Programme=Programme
    def set_Math(self,Math):
        if 0<=Math<=100:
            self.__Math=Math
        else:
            print("Invalid mark")
    def set_English(self,English):
        if 0<=English<=100:
            self.__English=English
        else:
            print("Invalid mark")
    def set_Science(self,Science):
        if 0<=Science<=100:
            self.__Science=Science
        else:
            print("Invalid mark")

    # REQUIREMENT 3: Method for calculating the average score.
    def average(self):
        return (self.__Math+self.__English+self.__Science)/3

    # REQUIREMENT 3: Method for determining the student's grade
    # from the average score.
    def grade(self):
        avg=self.average()
        if avg>=80:
            return "A"
        elif avg>=70:
            return "B"
        elif avg>=60:
            return "C"
        elif avg>=50:
            return "D"
        else:
            return "F"

    # REQUIREMENT 4 (Abstraction): Abstract method with no body.
    # Every subclass must implement it, and a Student object
    # cannot be created directly.
    @abstractmethod
    def display_info(self):
        pass
# ------------------------------------------------------
    # TASK 6: FLEXIBLE INTERFACE (METHOD OVERLOADING EQUIVALENT)
    # ------------------------------------------------------
    # *marks is a VARIABLE-LENGTH ARGUMENT. It collects any number of
    # marks into a tuple, so one method name accepts many call styles.
    # @staticmethod means it does not need a student object to be used.# ------------------------------------------------------
    # TASK 6: FLEXIBLE INTERFACE (METHOD OVERLOADING EQUIVALENT)
    # ------------------------------------------------------
    # *marks is a VARIABLE-LENGTH ARGUMENT. It collects any number of
    # marks into a tuple, so one method name accepts many call styles.
    # @staticmethod means it does not need a student object to be used.
    @staticmethod
    def calculate_average(*marks):

        # STEP 1: If one list or tuple was passed, such as
        # calculate_average([80,70,90]), unpack it into the marks.
        if len(marks)==1 and isinstance(marks[0],(list,tuple)):
            marks=marks[0]

        # STEP 2: Validation. At least one mark must be supplied.
        if len(marks)==0:
            raise ValueError("At least one mark is required")

        # STEP 3: Validation. Every mark must be a number from 0 to 100.
        for m in marks:
            if isinstance(m,bool) or not isinstance(m,(int,float)):
                raise TypeError("Marks must be numbers")
            if not 0<=m<=100:
                raise ValueError("Marks must be between 0 and 100")

        # STEP 4: Add the marks and divide by how many there are.
        return sum(marks)/len(marks)
    
    # ------------------------------------------------------
        # TASK 7: REPORT GENERATION
        # ------------------------------------------------------
        # Builds a readable report for ONE student and returns it as text.
        
    def generate_report(self):
            # STEP 1: A dashed line separates one student from the next.
            report="-"*40+"\n"
            # STEP 2: Student ID and full name.
            report+="Student ID: "+self.get_StudentID()+"\n"
            report+="Name: "+self.get_Fname()+" "+self.get_Lname()+"\n"
            # STEP 3: Programme.
            report+="Programme: "+self.get_Programme()+"\n"
            # STEP 4: Subject marks.
            report+="Math: "+str(self.get_Math())+"\n"
            report+="English: "+str(self.get_English())+"\n"
            report+="Science: "+str(self.get_Science())+"\n"
            # STEP 5: Average score and grade.
            report+="Average: "+str(round(self.average(),2))+"\n"
            report+="Grade: "+self.grade()+"\n"
            return report
    @staticmethod
    def calculate_average(*marks):
        

        # STEP 1: If one list or tuple was passed, such as
        # calculate_average([80,70,90]), unpack it into the marks.
        if len(marks)==1 and isinstance(marks[0],(list,tuple)):
            marks=marks[0]

        # STEP 2: Validation. At least one mark must be supplied.
        if len(marks)==0:
            raise ValueError("At least one mark is required")

        # STEP 3: Validation. Every mark must be a number from 0 to 100.
        for m in marks:
            if isinstance(m,bool) or not isinstance(m,(int,float)):
                raise TypeError("Marks must be numbers")
            if not 0<=m<=100:
                raise ValueError("Marks must be between 0 and 100")

        # STEP 4: Add the marks and divide by how many there are.
        return sum(marks)/len(marks)

# AIUStudent class inherits from Student and implements the
# required abstract method (display_info).
class AIUStudent(Student):
    def display_info(self):
        print("StudentID:",self.get_StudentID())
        print("Name:",self.get_Fname(),self.get_Lname())
        print("Programme:",self.get_Programme())
        print("Math:",self.get_Math())
        print("English:",self.get_English())
        print("Science:",self.get_Science())
        print("Average:",round(self.average(),2))
        print("Grade:",self.grade())
        
# TASK 3: PERFORMANCE ANALYZER AND COMPOSITION


# PerformanceAnalyzer uses COMPOSITION: it holds a list of Student
# objects ("has-a" relationship) instead of copying their data.
class PerformanceAnalyzer:

    # Receives the collection of student objects and stores the
    # reference to it. No student data is duplicated.
    def __init__(self,students):
        self.__students=students

    # Returns the student object with the highest average.
    # It asks each student for its own average() method.
    def highest_average(self):
        if not self.__students:
            return None
        return max(self.__students,key=lambda s:s.average())

    # Returns the student object with the lowest average.
    def lowest_average(self):
        if not self.__students:
            return None
        return min(self.__students,key=lambda s:s.average())
    # Builds the complete report: every student, then the class summary.
    def generate_report(self):
        # STEP 1: Stop early if there are no students.
        if not self.__students:
            return "No students to report on"
        report="STUDENT PERFORMANCE REPORT\n"
        # STEP 2: Each student creates its own report. This is
        # polymorphism, because ScholarshipStudent adds extra lines.
        for student in self.__students:
            report+=student.generate_report()
        # STEP 3: Class summary using the three analyzer methods.
        top=self.highest_average()
        low=self.lowest_average()
        report+="="*40+"\n"
        report+="CLASS PERFORMANCE SUMMARY\n"
        report+="Number of students: "+str(len(self.__students))+"\n"
        report+="Highest average: "+top.get_Fname()+" "+top.get_Lname()+" ("+str(round(top.average(),2))+")\n"
        report+="Lowest average: "+low.get_Fname()+" "+low.get_Lname()+" ("+str(round(low.average(),2))+")\n"
        report+="Overall class average: "+str(round(self.class_average(),2))+"\n"
        return report

    # Calculates the class average: the sum of every student's
    # average divided by the number of students.
    def class_average(self):
        if not self.__students:
            return 0
        total=0
        for s in self.__students:
            total+=s.average()
        return total/len(self.__students)
    
# TASK 4: INHERITANCE AND METHOD OVERRIDING

# ScholarshipStudent INHERITS from AIUStudent, so it automatically
# gets every getter, setter, average(), grade() and display_info().

class ScholarshipStudent(AIUStudent):

    # STEP 1: The constructor takes the usual student data plus the
    # new scholarship_amount. super()._init_() passes the usual
    # data up to the parent so it is not rewritten here.
    
    def __init__(self,StudentID,Fname,Lname,Programme,Math,English,Science,scholarship_amount):
        super().__init__(StudentID,Fname,Lname,Programme,Math,English,Science)
        self.__scholarship_amount=scholarship_amount

    # STEP 2: Getter and setter for the new private attribute
    # (same encapsulation style as the parent class).
    
    def get_scholarship_amount(self):
        return self.__scholarship_amount
    def set_scholarship_amount(self,amount):
        if amount>=0:
            self.__scholarship_amount=amount
        else:
            print("Invalid amount")

# STEP 3: New method (EXTENSION). It uses the inherited
# # average() method and returns True if the average is 85 or more.

    
    def is_eligible(self):
        return self.average()>=85

    # STEP 4: OVERRIDDEN method. It has the same name as the parent's
    # display_info(), but it changes the behaviour. super() first runs
    # the parent's version, then the scholarship details are added.
    
    def display_info(self):
        super().display_info()
        # OVERRIDDEN: reuses the parent's report with super(), then adds
    # the scholarship amount and eligibility ("where applicable").
    def generate_report(self):
        report=super().generate_report()
        report+="Scholarship amount: "+str(self.__scholarship_amount)+"\n"
        if self.is_eligible():
            report+="Scholarship eligibility: Eligible\n"
        else:
            report+="Scholarship eligibility: Not eligible\n"
        return report
        print("Scholarship amount:",self.__scholarship_amount)
        if self.is_eligible():
            print("Scholarship status: Eligible")
        else:
            print("Scholarship status: Not eligible")



# EXTRA FEATURE: PERMANENT STORAGE (CSV FILE)


FILE="student_data.csv"
HEADER=["StudentID","Fname","Lname","Programme","Math","English","Science",'']

# Converts a student object into a list so it can be written to the CSV.
#converts a student into a row.Only ScholarshipStudent has an amount.

def to_row(s):
    row= [s.get_StudentID(),s.get_Fname(),s.get_Lname(),s.get_Programme(),
            s.get_Math(),s.get_English(),s.get_Science()]
    if isinstance(s,ScholarshipStudent):
        row.append(s.get_scholarship_amount())
    else:
        row.append("")
    return row

# Reads all saved students from the CSV and creates AIUStudent objects.
#Rebuilds the correctstudent type from each row.
#an 8th value means ScholarshipStudent, otherwise AIUStudent.

def load_students():
    students=[]
    if not os.path.exists(FILE):
        return students
    with open(FILE,"r",newline="") as f:
        ro=csv.reader(f)
        next(ro,None)
        for row in ro:
            if len(row)==7:
                if len(row)>=8 and row[7]!="":
                    students.append(ScholarshipStudent(row[0],row[1],row[2],row[3],
                                int(row[4]),int(row[5]),int(row[6]),int(row[7])))
                else:
                    students.append(AIUStudent(row[0],row[1],row[2],row[3],
                                int(row[4]),int(row[5]),int(row[6])))
    return students

#Asks for the scholarship amount until valid number is entered.

def get_amount():
    while True:
        try:
            amount=int(input("Scholarship amount:"))
            if amount>=0:
                return amount
            print("Enter a non-negative amount")
        except ValueError:
            print("Enter numbers only")
            
#OPTION 1:now also asks whether the student has a scholarship.

def add_student():
    StudentID=input("StudentID:")
    for s in load_students():
        if s.get_StudentID()==StudentID:
            print("That ID already exists")
            return
    Fname=input("Fname:")
    Lname=input("Lname:")
    Programme=input("Programme:")
    Math=get_mark("Math")
    English=get_mark("English")
    Science=get_mark("Science")
    has_scholarship=input("Does the student have a scholarship? (Y/N):")
    if has_scholarship in 'Yy':
        amount=get_amount()
        s=ScholarshipStudent(StudentID,Fname,Lname,Programme,Math,English,Science,amount)
    else:
        s=AIUStudent(StudentID,Fname,Lname,Programme,Math,English,Science)
    save_student(s)
    print("Student saved permanently")
            
# Saves one student permanently by appending to the CSV file.

def save_student(s):
    new_file=not os.path.exists(FILE) or os.path.getsize(FILE)==0
    with open(FILE,"a",newline="") as f:
        wo=csv.writer(f)
        if new_file:
            wo.writerow(HEADER)
        wo.writerow(to_row(s))

# Asks for a mark and keeps asking until it is a number from 0 to 100.

def get_mark(subject):
    while True:
        try:
            m=int(input(subject+":"))
            if 0<=m<=100:
                return m
            print("Enter a mark between 0 and 100")
        except ValueError:
            print("Enter numbers only")



# MENU OPTIONS: ADD, VIEW AND DELETE


# OPTION 1: Takes student input, creates an AIUStudent object
# and saves it permanently.

def add_student():
    StudentID=input("StudentID:")
    for s in load_students():
        if s.get_StudentID()==StudentID:
            print("That ID already exists")
            return
    Fname=input("Fname:")
    Lname=input("Lname:")
    Programme=input("Programme:")
    Math=get_mark("Math")
    English=get_mark("English")
    Science=get_mark("Science")
    s=AIUStudent(StudentID,Fname,Lname,Programme,Math,English,Science)
    save_student(s)
    print("Student saved permanently")

# OPTION 2: Shows every saved student using the abstract
# method display_info() implemented in AIUStudent.

def view_students():
    students=load_students()
    if not students:
        print("No students saved yet")
    for s in students:
        s.display_info()
        print("-----")

# OPTION 3: Deletes one student by ID, after confirmation,
# and rewrites the CSV without that student.

def delete_student():
    StudentID=input("StudentID to delete:")
    students=load_students()
    remaining=[s for s in students if s.get_StudentID()!=StudentID]
    if len(remaining)==len(students):
        print("Student not found")
        return
    ch=input("Delete "+StudentID+"? (Y/N):")
    if ch in 'Yy':
        with open(FILE,"w",newline="") as f:
            wo=csv.writer(f)
            wo.writerow(HEADER)
            for s in remaining:
                wo.writerow(to_row(s))
        print("Student deleted")
        

# OPTION 4: Loads the saved students, passes them to the#
# PerformanceAnalyzer and prints the results.

def analyse_students():
    students=load_students()
    if not students:
        print("No students saved yet")
        return
    analyzer=PerformanceAnalyzer(students)
    top=analyzer.highest_average()
    low=analyzer.lowest_average()
    print("Highest average:",top.get_Fname(),top.get_Lname(),round(top.average(),2))
    print("Lowest average:",low.get_Fname(),low.get_Lname(),round(low.average(),2))
    print("Class average:",round(analyzer.class_average(),2))
    
 # DEMONSTRATION: shows what is inherited, extended and overridden.
 
def scholarship_demo():
    # Create one student above 85 and one below 85.
    s1=ScholarshipStudent("25/001","Jane","Doe","MDA",95,90,92,1000)
    s2=ScholarshipStudent("25/002","John","Smith","MDS",60,62,65,1000)

    # INHERITED: these methods are written in Student, not in ScholarshipStudent.
    print("INHERITED: average() and grade() from the parent class")
    print("Jane average:",round(s1.average(),2),"Grade:",s1.grade())
    print("John average:",round(s2.average(),2),"Grade:",s2.grade())

    # EXTENDED: is_eligible() exists only in ScholarshipStudent.
    print("\nEXTENDED: is_eligible() added by the subclass")
    print("Jane eligible:",s1.is_eligible())
    print("John eligible:",s2.is_eligible())

    # OVERRIDDEN: display_info() now prints extra scholarship lines.
    print("\nOVERRIDDEN: display_info() with scholarship details")
    s1.display_info()
    print("-----")
    s2.display_info()

    # Shows the subclass is still an AIUStudent and a Student.
    print("\nIs Jane an AIUStudent?",isinstance(s1,AIUStudent))
    print("Is Jane a Student?",isinstance(s1,Student))
    
# TASK 5: POLYMORPHISM


# Demonstrates polymorphism: different student types are stored
# in ONE list and the same method name is called on each of them.
def polymorphism_demo():

    # STEP 1: Create a mixed collection. The list holds two
    # AIUStudent objects and two ScholarshipStudent objects.
    students=[
        AIUStudent("25/101","Mary","Akello","MDA",70,65,72),
        ScholarshipStudent("25/102","James","Okello","MDS",95,92,90,1000),
        AIUStudent("25/103","Grace","Nabirye","MDA",55,60,58),
        ScholarshipStudent("25/104","Peter","Kato","MDS",60,62,65,1000)
    ]

    # STEP 2: Loop through the list and call display_info() on each
    # object. The code is the same every time, but Python chooses the
    # version of display_info() that belongs to the actual object.
    for s in students:
        print("Object type:",type(s).__name__)
        s.display_info()
        print("-----")

    # STEP 3: PerformanceAnalyzer (Task 3) also works with the mixed
    # list, because every object is a Student with an average() method.
    analyzer=PerformanceAnalyzer(students)
    print("Class average of mixed group:",round(analyzer.class_average(),2))
    
# TASK 6: METHOD OVERLOADING AND FLEXIBLE INTERFACES


# Calls the SAME method with different kinds of input.
def overloading_demo():

    # STEP 1: Three marks supplied separately.
    print("Three marks:",round(Student.calculate_average(80,70,90),2))

    # STEP 2: A different number of marks, same method name.
    print("Two marks:",round(Student.calculate_average(85,75),2))
    print("Five marks:",round(Student.calculate_average(60,70,80,90,100),2))

    # STEP 3: A single list of marks.
    print("List of marks:",round(Student.calculate_average([88,92,79,95]),2))

    # STEP 4: Works through a student object too (inherited).
    s=AIUStudent("25/201","Anna","Mukasa","MDA",70,80,90)
    print("Through an object:",round(s.calculate_average(70,80),2))

    # STEP 5: Invalid inputs. Each one is rejected with a message
    # instead of crashing the program.
    bad_inputs=[(),(80,"abc"),(80,120),(-5,50)]
    for b in bad_inputs:
        try:
            Student.calculate_average(*b)
        except (ValueError,TypeError) as e:
            print("Rejected",b,"->",e)
    # OPTION 8: Loads saved students, builds the report, shows it on
# screen and saves a copy to a text file.
def report_option():
    students=load_students()
    if not students:
        print("No students saved yet")
        return
    analyzer=PerformanceAnalyzer(students)
    report=analyzer.generate_report()
    print(report)
    with open("student_report.txt","w") as f:
        f.write(report)
    print("Report saved to student_report.txt")

# Main menu loop that connects all the options.
def menu():
    while True:
        print("\n1. Add student")
        print("2. View all students")
        print("3. Delete a student")
        print("4. analyse class performance")
        print("5. Scholarship demonstration")
        print("6. Polymorphism demonstration")
        print("7. Method overloading demonstration")
        print("8. Generate report")
        print("9. Exit")
        choice=input("Choose option:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            delete_student()
        elif choice=="4":
            analyse_students()
        elif choice=="5":
            scholarship_demo()
        elif choice=="6":
            polymorphism_demo()
        elif choice=="7":
            overloading_demo()
        elif choice=="8":
            report_option()
        elif choice=="9":
            print("Exiting...")
            break
        else:
            print("Invalid option")

menu()