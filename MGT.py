import os  # Importing the os module for operating system-related functionalities

"""
MARKSHEET GENERATOR TOOL:

The marksheet generator is a Python project designed to automate the process of generating student mark sheets 
within a terminal environment. 
This project simplifies the task of creating mark sheets for educational institutions by allowing users to input 
student details and marks for various subjects, and then automatically generating comprehensive mark sheets.
"""

# Clearing the console screen (for Windows systems)
os.system("cls")

"""2nd Semester All Subjects Details"""

# theory subjects
subject_1_code = "KAS201T"
subject_1_name = "Engineering Physics"
subject_1_type = "Theory"
subject_1_total_marks = 150
subject_1_credit_point = 4

subject_2_code = "KAS203T"
subject_2_name = "Engineering Mathematics-II"
subject_2_type = "Theory"
subject_2_total_marks = 150
subject_2_credit_point = 4

subject_3_code = "KEC201T"
subject_3_name = "Emerging Domain in Electronics Engineering"
subject_3_type = "Theory"
subject_3_total_marks = 150
subject_3_credit_point = 3

subject_4_code = "KME201T"
subject_4_name = "Fundamentals of Mechanical Enginnering & Mechatronics"
subject_4_type = "Theory"
subject_4_total_marks = 150
subject_4_credit_point = 3

subject_5_code = "KMC202"
subject_5_name = "Emerging Technology for Engineering"
subject_5_type = "Theory"
subject_5_total_marks = 50
subject_5_credit_point = 2

# practical subjects
subject_6_code = "KAS251P"
subject_6_name = "Engineering Physics Lab"
subject_6_type = "Practical"
subject_6_total_marks = 50
subject_6_credit_point = 1

subject_7_code = "KEC251P"
subject_7_name = "Electronics Engineering Lab"
subject_7_type = "Practical"
subject_7_total_marks = 50
subject_7_credit_point = 1

subject_8_code = "KAS254P"
subject_8_name = "English Language Lab"
subject_8_type = "Practical"
subject_8_total_marks = 50
subject_8_credit_point = 1

subject_9_code = "KCE251P"
subject_9_name = "Engineering Graphics & Design Lab"
subject_9_type = "Practical"
subject_9_total_marks = 100
subject_9_credit_point = 1

# calculating total marks from adding theory and practical subjects
total_marks = (
    subject_1_total_marks
    + subject_2_total_marks
    + subject_3_total_marks
    + subject_4_total_marks
    + subject_5_total_marks
    + subject_6_total_marks
    + subject_7_total_marks
    + subject_8_total_marks
    + subject_9_total_marks
)  # 900

# calculating total credits by adding all credits from credit based subjects
total_credits = (
    subject_1_credit_point
    + subject_2_credit_point
    + subject_3_credit_point
    + subject_4_credit_point
    + subject_5_credit_point
    + subject_6_credit_point
    + subject_7_credit_point
    + subject_8_credit_point
    + subject_9_credit_point
)  # 20

# additional subjects, non-credit subjects
subject_10_code = "KNC201"
subject_10_name = "Soft Skill II"
subject_10_type = "Additional"
subject_10_total_marks = 50

# Clearing the console screen (for Windows systems)
os.system("cls")
print(
    """         
                ***Enter Student Details***          
"""
)

"""Taking student details as input from user"""


# Function to validate input as string
def is_valid_string(user_input):
    valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,'"
    for char in user_input:
        if char not in valid_characters:
            return False
    return True


def get_string_input(prompt):
    while True:
        user_input = input(prompt)
        if is_valid_string(user_input):
            return user_input
        else:
            print("Please enter a valid string.")


# taking university/board name
university_name = get_string_input("Enter University Name: ")
print()  # Printing an empty line for better readability

# taking institute/college name
institute_name = get_string_input("Enter Institute Name: ")
print()  # Printing an empty line for better readability

# taking course name
course_name = get_string_input("Enter Course Name: ")
print()  # Printing an empty line for better readability

# taking branch name
branch_name = get_string_input("Enter Branch Name: ")
print()  # Printing an empty line for better readability

## Taking session and validating it by validate_session() function
# Prompting the user to input the session in the format YYYY-YY
session = input("Enter Session (Format: YYYY-YY): ")


# Function to validate session format
def validate_session(session):

    # Session validation: Format YYYY-YY (e.g., 2020-24)
    parts = session.split("-")  # Splitting session into parts separated by '-'

    # Check if session has exactly 2 parts
    if len(parts) != 2:
        return False

    # Check if all parts are composed of digits
    for part in parts:
        if not part.isdigit():
            return False

    # Check if the first part (year) has 4 digits and the second part (year range) has 2 digits
    if len(parts[0]) != 4 or len(parts[1]) != 2:
        return False

    return True  # If all conditions are met, session format is valid


# Session validation
# Loop until a valid session is entered
while not validate_session(session):
    # Informing the user about the invalid session format
    print(
        """
        Invalid session format. Please enter the session in the format YYYY-YY (e.g., 2020-24).
        """
    )
    # Prompting the user to input the session again
    session = input("Enter Session (Format: YYYY-YY): ")

# Printing an empty line for better readability
print()


## Taking semester and validating it by validate_semester() function
# Prompting the user to input the semester (single digit, 1-8)
semester = input("Enter Semester (Single digit, 1-8): ")


# Function to validate semester format
def validate_semester(semester):
    # Semester validation: Single digit (1-9)
    # Check if semester consists of a single digit
    if len(semester) != 1:
        return False

    # Check if it is a digit
    if not semester.isdigit():
        return False

    # Check if the digit is in the range 1-8
    if semester not in "12345678":
        return False

    return True  # If all conditions are met, semester format is valid


# Semester validation
# Loop until a valid semester is entered
while not validate_semester(semester):
    # Informing the user about the invalid semester format
    print(
        """
        Invalid semester format. Please enter a single digit between 1 and 8.
        """
    )
    # Prompting the user to input the semester again
    semester = input("Enter Semester (Single digit, 1-8): ")

# Printing an empty line for better readability
print()


## Taking roll number and validating it by validate_roll_number() function
# Prompting the user to input the roll number (13 digits)
roll_number = input("Enter Roll Number (13 digits): ")


# Function to validate roll number format
def validate_roll_number(roll_number):
    # Roll number validation: (e.g., 2005020100032) 13 digits
    return roll_number.isdigit() and len(roll_number) == 13


# Roll number validation
# Loop until a valid roll number is entered
while not validate_roll_number(roll_number):
    # Informing the user about the invalid roll number format
    print(
        """
        Invalid roll number format. Please enter the roll number in 13 digits.
        """
    )
    # Prompting the user to input the roll number again
    roll_number = input("Enter Roll Number (13 digits): ")

# Printing an empty line for better readability
print()


## Taking enrollment number and validating it by validate_enrollment_number() function
# Prompting the user to input the enrollment number (15 digits)
enrollment_number = input("Enter Enrollment Number (15 digits): ")


# Function to validate enrollment number format
def validate_enrollment_number(enrollment_number):
    # Enrollment number validation: (e.g., 200502010053823) 15 digits
    return enrollment_number.isdigit() and len(enrollment_number) == 15


# Enrollment number validation
# Loop until a valid enrollment number is entered
while not validate_enrollment_number(enrollment_number):
    # Informing the user about the invalid enrollment number format
    print(
        """
        Invalid enrollment number format. Please enter the enrollment number in 15 digits.
        """
    )
    # Prompting the user to input the enrollment number again
    enrollment_number = input("Enter Enrollment Number (15 digits): ")

# Printing an empty line for better readability
print()

# taking student name from user
student_name = get_string_input("Enter Student Name: ")
print()  # Printing an empty line for better readability

# taking father's name form user
father_name = get_string_input("Enter Father's Name: ")
print()  # Printing an empty line for better readability

# taking mother's name from user
mother_name = get_string_input("Enter Mother's Name: ")
print()  # Printing an empty line for better readability


## Taking date-of-birth from the user and validating it by validate_date() function
# Prompting the user to input the date of birth in the format DD-MM-YYYY
date_of_birth = input("Enter Date of Birth (DD-MM-YYYY): ")


# Function to validate date
def validate_date(date):
    # Date validation: DD-MM-YYYY format
    # Split the date string into parts separated by '-'
    parts = date.split("-")

    # Check if the date string has exactly 3 parts (day, month, year)
    if len(parts) != 3:
        return False

    # Check if all parts are composed of digits
    for part in parts:
        if not part.isdigit():
            return False

    # Check if the day part has 2 digits
    if len(parts[0]) != 2:
        return False

    # Check if the month part has 2 digits
    if len(parts[1]) != 2:
        return False

    # Check if the year part has 4 digits
    if len(parts[2]) != 4:
        return False

    # If all conditions are met, the date format is valid
    return True


# Date of Birth validation: Basic format check
# Loop until a valid date of birth is entered
while not validate_date(date_of_birth):
    # Informing the user about the invalid date format
    print(
        """
        Invalid date format. Please enter the date in DD-MM-YYYY format.
        """
    )
    # Prompting the user to input the date of birth again
    date_of_birth = input("Enter Date of Birth (DD-MM-YYYY): ")

# Printing an empty line for better readability
print()


## Taking gender from the user and validating it by values: "male" and "female" from a list.
# Prompting the user to input the gender (Male/Female)
gender = input("Enter Gender (Male/Female): ")

# Gender validation: Male or Female
# Loop until a valid gender is entered
while gender.lower() not in ["male", "female"]:
    # Informing the user about the invalid gender
    print(
        """
        Invalid gender. Please enter Male or Female.
        """
    )
    # Prompting the user to input the gender again
    gender = input("Enter Gender (Male/Female): ")

# Printing an empty line for better readability
print()


## Taking pincode from the user and validating it by validate_pincode() function
# Prompting the user to input the pincode
pincode = input("Enter Pin Code: ")


# Function to validate pincode
def validate_pincode(pincode):
    # Ensure pincode is made up of 6 digits
    is_all_digits = pincode.isdigit()  # Check if all characters are digits
    is_length_six = len(pincode) == 6  # Check if pincode length is 6

    return is_all_digits and is_length_six


# Pincode validation
# Loop until a valid pincode is entered
while not validate_pincode(pincode):
    # Informing the user about the invalid pincode
    print(
        """
        Invalid pin code. Please enter a 6-digit pin code.
        """
    )
    # Prompting the user to input the pincode again
    pincode = input("Enter Pin Code: ")

# Printing an empty line for better readability
print()


# Pausing the script to wait for user input (for Windows systems)
os.system("pause")
# Clearing the console screen (for Windows systems)
os.system("cls")
print(
    """         
                ***Enter Internal Marks***          
"""
)


# Function to validate internal marks the marks based on user input
def input_and_validate_internal_marks(subject_name, max_marks):

    marks = -1  # Initializing marks to an invalid value to enter the loop

    while marks < 0 or marks > max_marks:  # Loop until valid marks are entered
        marks = int(
            input(f"{subject_name} (0-{max_marks}): ")
        )  # Prompting the user for marks input
        if marks < 0 or marks > max_marks:  # Checking if the entered marks are valid
            print(
                f"""
                Marks should be between 0 and {max_marks}.  # Informing the user about the valid range of marks
                """
            )
    print()  # Printing an empty line for better readability
    # Printing an empty line for better readability
    return marks  # Returning the validated marks


# Taking internal marks for each subject from the user input
subject_1_internal_marks = input_and_validate_internal_marks(subject_1_name, 50)
subject_2_internal_marks = input_and_validate_internal_marks(subject_2_name, 50)
subject_3_internal_marks = input_and_validate_internal_marks(subject_3_name, 50)
subject_4_internal_marks = input_and_validate_internal_marks(subject_4_name, 50)
subject_5_internal_marks = input_and_validate_internal_marks(subject_5_name, 25)
subject_6_internal_marks = input_and_validate_internal_marks(subject_6_name, 25)
subject_7_internal_marks = input_and_validate_internal_marks(subject_7_name, 25)
subject_8_internal_marks = input_and_validate_internal_marks(subject_8_name, 25)
subject_9_internal_marks = input_and_validate_internal_marks(subject_9_name, 50)
subject_10_internal_marks = input_and_validate_internal_marks(subject_10_name, 25)

# Pausing the script to wait for user input (for Windows systems)
os.system("pause")
# Clearing the console screen (for Windows systems)
os.system("cls")
print(
    """         
                ***Enter External Marks***          
"""
)


# Function to validate external marks based on user input
def input_and_validate_external_marks(subject_name, max_marks):
    marks = -1  # Initializing marks to an invalid value to enter the loop
    while marks < 0 or marks > max_marks:  # Loop until valid marks are entered
        marks = int(
            input(f"{subject_name} (0-{max_marks}): ")
        )  # Prompting the user for marks input
        if marks < 0 or marks > max_marks:  # Checking if the entered marks are valid
            print(
                f"""
                External marks should be between 0 and {max_marks}.  # Informing the user about the valid range of marks
                """
            )
    print()  # Printing an empty line for better readability
    # Printing an empty line for better readability
    return marks  # Returning the validated marks


# Taking external marks for each subject from the user input
subject_1_external_marks = input_and_validate_external_marks(subject_1_name, 100)
subject_2_external_marks = input_and_validate_external_marks(subject_2_name, 100)
subject_3_external_marks = input_and_validate_external_marks(subject_3_name, 100)
subject_4_external_marks = input_and_validate_external_marks(subject_4_name, 100)
subject_5_external_marks = input_and_validate_external_marks(subject_5_name, 25)
subject_6_external_marks = input_and_validate_external_marks(subject_6_name, 25)
subject_7_external_marks = input_and_validate_external_marks(subject_7_name, 25)
subject_8_external_marks = input_and_validate_external_marks(subject_8_name, 25)
subject_9_external_marks = input_and_validate_external_marks(subject_9_name, 50)
subject_10_external_marks = input_and_validate_external_marks(subject_10_name, 25)


# Pausing the script to wait for user input (for Windows systems)
os.system("pause")
# Clearing the console screen (for Windows systems)
os.system("cls")
print(
    """         
                ***Enter Passing Year***          
"""
)
# taking passing year as input from the user
passing_year = input("Enter Passing Year: ")
print()  # Printing an empty line for better readability


# calculating total obtained marks for each subject from adding internal and external marks
subject_1_obtained_marks = subject_1_internal_marks + subject_1_external_marks
subject_2_obtained_marks = subject_2_internal_marks + subject_2_external_marks
subject_3_obtained_marks = subject_3_internal_marks + subject_3_external_marks
subject_4_obtained_marks = subject_4_internal_marks + subject_4_external_marks
subject_5_obtained_marks = subject_5_internal_marks + subject_5_external_marks
subject_6_obtained_marks = subject_6_internal_marks + subject_6_external_marks
subject_7_obtained_marks = subject_7_internal_marks + subject_7_external_marks
subject_8_obtained_marks = subject_8_internal_marks + subject_8_external_marks
subject_9_obtained_marks = subject_9_internal_marks + subject_9_external_marks

# calculating total marks obtained by the student by adding obtained marks in all subjects
total_mark_obtained = (
    subject_1_obtained_marks
    + subject_2_obtained_marks
    + subject_3_obtained_marks
    + subject_4_obtained_marks
    + subject_5_obtained_marks
    + subject_6_obtained_marks
    + subject_7_obtained_marks
    + subject_8_obtained_marks
    + subject_9_obtained_marks
)

# calculating percentage of each subject
subject_1_percentage = (subject_1_obtained_marks / subject_1_total_marks) * 100
subject_2_percentage = (subject_2_obtained_marks / subject_2_total_marks) * 100
subject_3_percentage = (subject_3_obtained_marks / subject_3_total_marks) * 100
subject_4_percentage = (subject_4_obtained_marks / subject_4_total_marks) * 100
subject_5_percentage = (subject_5_obtained_marks / subject_5_total_marks) * 100
subject_6_percentage = (subject_6_obtained_marks / subject_6_total_marks) * 100
subject_7_percentage = (subject_7_obtained_marks / subject_7_total_marks) * 100
subject_8_percentage = (subject_8_obtained_marks / subject_8_total_marks) * 100
subject_9_percentage = (subject_9_obtained_marks / subject_9_total_marks) * 100

# Calculating overall percentage
overall_percentage = (total_mark_obtained / total_marks) * 100

# Checking passing status based on overall percentage
# If the overall percentage is greater than or equal to 40%
if overall_percentage >= 40:
    passing_status = "Passed"  # Set passing_status to "Passed"
else:
    passing_status = "Failed"  # Otherwise, set passing_status to "Failed"


def calculate_grade(percentage):
    # Determine the grade based on the percentage
    if percentage >= 90:
        return "A+"  # Return "A+" if percentage is 90 or above
    elif percentage >= 80:
        return "A"  # Return "A" if percentage is between 80 and 89
    elif percentage >= 70:
        return "B+"  # Return "B+" if percentage is between 70 and 79
    elif percentage >= 60:
        return "B"  # Return "B" if percentage is between 60 and 69
    elif percentage >= 50:
        return "C"  # Return "C" if percentage is between 50 and 59
    elif percentage >= 45:
        return "D"  # Return "D" if percentage is between 45 and 49
    elif percentage >= 40:
        return "E"  # Return "E" if percentage is between 40 and 44
    else:
        return "F"  # Return "F" if percentage is below 40


# calculating grade for each suject by using calculate_grade() function
subject_1_grade = calculate_grade(subject_1_percentage)
subject_2_grade = calculate_grade(subject_2_percentage)
subject_3_grade = calculate_grade(subject_3_percentage)
subject_4_grade = calculate_grade(subject_4_percentage)
subject_5_grade = calculate_grade(subject_5_percentage)
subject_6_grade = calculate_grade(subject_6_percentage)
subject_7_grade = calculate_grade(subject_7_percentage)
subject_8_grade = calculate_grade(subject_8_percentage)
subject_9_grade = calculate_grade(subject_9_percentage)
subject_10_grade = "  "


# Function to calculate Grade Points
def calculate_grade_points(grade):
    # Determine the grade points based on the grade
    if grade == "A+":
        return 10  # Return 10 if the grade is A+
    elif grade == "A":
        return 9  # Return 9 if the grade is A
    elif grade == "B+":
        return 8  # Return 8 if the grade is B+
    elif grade == "B":
        return 7  # Return 7 if the grade is B
    elif grade == "C":
        return 6  # Return 6 if the grade is C
    elif grade == "D":
        return 5  # Return 5 if the grade is D
    elif grade == "E":
        return 4  # Return 4 if the grade is E
    elif grade == "F":
        return 0  # Return 0 if the grade is


# Calculate Grade Points for each subject
subject_1_grade_points = calculate_grade_points(subject_1_grade)
subject_2_grade_points = calculate_grade_points(subject_2_grade)
subject_3_grade_points = calculate_grade_points(subject_3_grade)
subject_4_grade_points = calculate_grade_points(subject_4_grade)
subject_5_grade_points = calculate_grade_points(subject_5_grade)
subject_6_grade_points = calculate_grade_points(subject_6_grade)
subject_7_grade_points = calculate_grade_points(subject_7_grade)
subject_8_grade_points = calculate_grade_points(subject_8_grade)
subject_9_grade_points = calculate_grade_points(subject_9_grade)

# calculating total earned points in each subject by adding credit points and grade points
subject_1_total_earned_points = subject_1_credit_point * subject_1_grade_points
subject_2_total_earned_points = subject_2_credit_point * subject_2_grade_points
subject_3_total_earned_points = subject_3_credit_point * subject_3_grade_points
subject_4_total_earned_points = subject_4_credit_point * subject_4_grade_points
subject_5_total_earned_points = subject_5_credit_point * subject_5_grade_points
subject_6_total_earned_points = subject_6_credit_point * subject_6_grade_points
subject_7_total_earned_points = subject_7_credit_point * subject_7_grade_points
subject_8_total_earned_points = subject_8_credit_point * subject_8_grade_points
subject_9_total_earned_points = subject_9_credit_point * subject_9_grade_points

# calculating total earned points by adding earned points of all subjects
total_earned_point = (
    subject_1_total_earned_points
    + subject_2_total_earned_points
    + subject_3_total_earned_points
    + subject_4_total_earned_points
    + subject_5_total_earned_points
    + subject_6_total_earned_points
    + subject_7_total_earned_points
    + subject_8_total_earned_points
    + subject_9_total_earned_points
)

# Calculate SGPA from dividing total earned points by total credits
sgpa = total_earned_point / total_credits

# Check for grace status
grace_status = ""

# Counting the number of subjects with marks between 31 and 32
# Check if subject marks are within the range and convert the result to 0 or 1
subjects_within_range_count = (
    (31 <= subject_1_obtained_marks <= 32)
    + (31 <= subject_2_obtained_marks <= 32)
    + (31 <= subject_3_obtained_marks <= 32)
    + (31 <= subject_4_obtained_marks <= 32)
    + (31 <= subject_5_obtained_marks <= 32)
    + (31 <= subject_6_obtained_marks <= 32)
    + (31 <= subject_7_obtained_marks <= 32)
    + (31 <= subject_8_obtained_marks <= 32)
    + (31 <= subject_9_obtained_marks <= 32)
)

# Check if candidate has got 31 >= marks <= 32 in more than one subject

# If candidate has got marks between 31 and 32 in more than one subject
if subjects_within_range_count >= 2:
    grace_status = "Fail"  # Set grace_status to "Fail"

# If candidate has got marks between 31 and 32 in only one subject
elif subjects_within_range_count == 1:
    grace_status = "Passed with Grace(Promoted)"  # Set grace_status to "Passed with Grace(Promoted)"

# If candidate has not got marks between 31 and 32 in any subject
else:
    grace_status = "Passed"  # Set grace_status to "Passed"


os.system("pause")
os.system("cls")

print(
    f"""
                                    {university_name.upper()}
===================================================================================================================                                                              
Institute Name  :  {institute_name.upper()}
Course Name     :  {course_name.upper(): <40} Branch Name         :  {branch_name.upper()}
Session         :  {session: <40} Semester            :  {semester}
Roll Number     :  {roll_number: <40} Enrollment Number   :  {enrollment_number}
Student Name    :  {student_name.upper(): <40} Father's Name       :  {father_name.upper()}
Mother's Name   :  {mother_name.upper(): <40} Date of Birth       :  {date_of_birth.upper()}
Gender          :  {gender.upper(): <40} Pin Code            :  {pincode}

===================================================================================================================
 __________________________________________________________________________________________________________________
| Code     | Name                                                   | Type           | Internal | External | Grade |
|----------|--------------------------------------------------------|----------------|----------|----------|-------|
| {subject_1_code: <7}  | {subject_1_name: <54} | {subject_1_type: <14} | {subject_1_internal_marks: <8} | {subject_1_external_marks: <8} | {subject_1_grade: <5} |
| {subject_2_code: <7}  | {subject_2_name: <54} | {subject_2_type: <14} | {subject_2_internal_marks: <8} | {subject_2_external_marks: <8} | {subject_2_grade: <5} |
| {subject_3_code: <7}  | {subject_3_name: <54} | {subject_3_type: <14} | {subject_3_internal_marks: <8} | {subject_3_external_marks: <8} | {subject_3_grade: <5} |
| {subject_4_code: <7}  | {subject_4_name: <54} | {subject_4_type: <14} | {subject_4_internal_marks: <8} | {subject_4_external_marks: <8} | {subject_4_grade: <5} |
| {subject_5_code: <7}  | {subject_5_name: <54} | {subject_5_type: <14} | {subject_5_internal_marks: <8} | {subject_5_external_marks: <8} | {subject_5_grade: <5} |
| {subject_6_code: <7}  | {subject_6_name: <54} | {subject_6_type: <14} | {subject_6_internal_marks: <8} | {subject_6_external_marks: <8} | {subject_6_grade: <5} |
| {subject_7_code: <7}  | {subject_7_name: <54} | {subject_7_type: <14} | {subject_7_internal_marks: <8} | {subject_7_external_marks: <8} | {subject_7_grade: <5} |
| {subject_8_code: <7}  | {subject_8_name: <54} | {subject_8_type: <14} | {subject_8_internal_marks: <8} | {subject_8_external_marks: <8} | {subject_8_grade: <5} |
| {subject_9_code: <7}  | {subject_9_name: <54} | {subject_9_type: <14} | {subject_9_internal_marks: <8} | {subject_9_external_marks: <8} | {subject_9_grade: <5} |
| {subject_10_code: <7}  | {subject_10_name: <54} | {subject_10_type: <14} | {subject_10_internal_marks: <8} | {subject_10_external_marks: <8} | {subject_10_grade: <5} |
--------------------------------------------------------------------------------------------------------------------
Result: {passing_status: <40} Total Marks: {total_marks: <34} Marks Obtained: {total_mark_obtained} 
Passing Year: {passing_year: <34} SGPA: {format(sgpa, '.2f'): <41} Percentage: {format(overall_percentage, '.2f')}   
Grace Status: {grace_status} 
"""
)

# Pausing the script to wait for user input (for Windows systems)
os.system("pause")
