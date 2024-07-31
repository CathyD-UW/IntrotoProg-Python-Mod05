# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#     CDuPuis, 7/30/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# Functions
def load_data(file_name):
    """ Load data from JSON file """
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: {file_name} not found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print(f"Error: {file_name} is not a valid JSON file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def save_data(file_name, data):
    """ Save data to JSON file """
    try:
        file = open(file_name, 'w')
        try:
            json.dump(data, file, indent=4)
        except TypeError as te:
            print(f"Type error while writing data: {te}")
        except ValueError as ve:
            print(f"Value error while writing data: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred while writing data: {e}")
        finally:
            file.close()
        print(f"Data saved to {file_name}")
        print("Saved data:")
        for student in data:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
    except IOError as ioe:
        print(f"I/O error while opening file: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred while opening the file: {e}")

# Load initial data
students = load_data(FILE_NAME)

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
            if not student_first_name.isalpha():
                raise ValueError("First name must only contain letters.")
        except ValueError as ve:
            print(f"Input error: {ve}")
            continue

        try:
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
            if not student_last_name.isalpha():
                raise ValueError("Last name must only contain letters.")
        except ValueError as ve:
            print(f"Input error: {ve}")
            continue

        try:
            course_name = input("Please enter the name of the course: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")
        except ValueError as ve:
            print(f"Input error: {ve}")
            continue

        student_data = {
            "FirstName": student_first_name,
            "LastName": student_last_name,
            "CourseName": course_name
        }
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        if not students:
            print("No student data available.")
        else:
            print("Current registered students:")
            for student in students:
                print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        save_data(FILE_NAME, students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
