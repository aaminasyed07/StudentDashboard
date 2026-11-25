StudentName="Aamina"
StudentAge="18"
StudentAttendance="100%"
print("======================")
print("StudentDashBoard")
print("======================")
print(StudentName)
print(StudentAge)
print(StudentAttendance)
print("StudentDashBoardcreatedSuccesfully")

Studentid= int(input("Enter Student ID: "))
Studentname=input("Enter your Name: ")
subject1=input("Enter subject 1: ")
subject2=input("Enter subject 2: ")
subject3=input("Enter subject 3: ")
NumofHrspersubject1=int(input("Enter NumofHrsPersubject1: "))
NumofHrspersubject2=int(input("Enter NumofHrsPersubject2: "))
NumofHrspersubject3=int(input("Enter NumofHrsPersubject3: "))
Date=input("Enter your Date : ")
total_hours=NumofHrspersubject1+NumofHrspersubject2+NumofHrspersubject3
average_hours=total_hours/3


print("======================")
print("Student ID: ", Studentid)
print("Student Name: ", Studentname)
print("Subject 1: ", subject1)
print("Subject 2: ", subject2)
print("Subject 3: ", subject3)
print("NumofHrsPersubject1: ", NumofHrspersubject1)
print("NumofHrsPersubject2: ", NumofHrspersubject2)
print("NumofHrsPersubject3: ", NumofHrspersubject3)
print("Total Hours: ", total_hours)
print("Average Hours: ", average_hours)

