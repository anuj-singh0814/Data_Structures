## Create a Dictionary of Student Marks

student_marks = {"AK":98, "Ashwin": 56, "karthik": 88, "Deepak": 76, "Mohini": 48 }

# Ask the user to input a student's name
student_name = input("Enter a student's name: ")

# Retrieve and display the marks if the student exists
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Sorry, '{student_name}' is not found in the records.")



