# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Ntsao,12/4/2024,Created Script
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


# Create a Person Class
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.

    ChangeLog:
    - Ntsao, 12.4.2024: Created the class.
    """

    # Add first_name and last_name properties to the constructor
    def __init__(self, first_name:str = "", last_name:str = ""):
        self.first_name = first_name
        self.last_name = last_name

    #  Create a getter and setter for the first_name property
    @property
    def first_name(self):
        """
            Returns the first_name as a title
            return: The first_name, formatted as a title
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
            Sets the first name, executes validation

        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should only contain alphabetical characters.")

    #  Create a getter and setter for the last_name property
    @property
    def last_name(self):
        """
            Returns the last_name as a title
            return: The last_name, formatted as a title
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
            Sets the last name, executes validations

        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should only contain alphabetical characters.")

    # Override the __str__() method to return Person data
    def __str__(self):
        """
            Returns first name and last name for class Person

        """
        return f"{self.first_name},{self.last_name}"

# Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection data about students

    ChangeLog: (Who, When, What)
    Ntsao,12.4.2024,Created Class
    Ntsao,12.4.2024,Added properties and private attributes
    """
    # call to the Person constructor and pass it the first_name and last_name data
    # add a assignment to the course_name property using the course_name parameter
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        super().__init__(first_name=first_name,last_name=last_name )
        self.course_name = course_name

# add the getter for course_name
    @property
    def course_name(self):
        """
            Returns the course_name as a title
            return: The course_name, formatted as a title
        """
        return self.__course_name.title()

# add the setter for course_name
    @course_name.setter
    def course_name(self, value: str):
        """
            Sets the course name

        """
        self.__course_name = value

# Override the __str__() method to return the Student data
    def __str__(self):
        """
            Returns first name and last name for class Person
            also returns course name

        """
        return f"{super().__str__()},{self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Ntsao,12.4.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[Student])->list[Student]:
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function

        return: list
        """
        file_data = []
        file=None
        try:
            file = open(file_name, "r")
            file_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and not file.closed:
                file.close()
        for row in file_data:
            student_data.append(
                Student(row["FirstName"], row["LastName"], row["CourseName"])
            )
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[Student]):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function

        param file_name: string data with name of file to write to
        param student_data: list of dictionary rows to be writen to the file

        return: None
        """
        file_data = []
        for student in student_data:
            file_data.append({'first_name': student.first_name,
                              'last_name': student.last_name,
                              'course_name': student.course_name})

        file=None
        try:
            file = open(file_name, "w")
            json.dump(file_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Ntsao,12.4.2024,Created Class
    Ntsao,12.4.2024,Added menu output and input functions
    Ntsao,12.4.2024,Added a function to display the data
    Ntsao,12.4.2024,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list[Student]):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list[Student])->list[Student]:
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Ntsao,12.4.2024,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student = Student(student_first_name,
                              student_last_name,
                              course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body
# Define the Data Variables
students: list[Student] = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
