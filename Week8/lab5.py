#W6D1 Class Lab

#Bradley Coppinger 
#Lab 8
#9/4/2024

#In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file: lab5.txt

# Variable List
#file_path - The path to the text file (lab5_students.txt) that contains student data.
#ids - A list that stores all student IDs (from the ID column in the file).
#last_names - A list that stores all students' last names (from the LastName column in the file).
##first_names - A list that stores all students' first names (from the FirstName column in the file).
#class1 - A list that stores the first class that each student is enrolled in (from the Class1 column in the file).
#class2 - A list that stores the second class that each student is enrolled in (from the Class2 column in the file).
#class3 - A list that stores the third class that each student is enrolled in (from the Class3 column in the file).


# Part 1: Display Menu Function
# This function displays the menu options to the user and returns their choice
def display_menu():
    print("1. See All Student Report")
    print("2. Search for a Student [ID]")
    print("3. Search for a Student [Last]")
    print("4. View a Class Roster [class1, class2, and class3]")
    print("5. Exit/Quit Program")
    return input("Choose an option (1-5): ")

# Part 2: Read Data from File and Store in Parallel Lists
# Lists
ids = []
last_names = []
first_names = []
class1 = []
class2 = []
class3 = []

#file path 
file_path = r'Week8\lab5_students.txt'

# Open the file containing student data
with open(file_path, 'r') as file:
    for line in file:
        data = line.strip().split(',')  # Split the line by commas
        # Append the data to the respective lists
        ids.append(data[0])
        last_names.append(data[1])
        first_names.append(data[2])
        class1.append(data[3])
        class2.append(data[4])
        class3.append(data[5])

# Part 3: Sequential Search Function for Course Roster
# This function allows the user to search for a class, and if the class exists,
# it displays all students enrolled in that class.
def sequential_search(course):
    found_class = []  # List to store students found in the course
    course = course.lower()  # Convert input to lowercase to make search case-insensitive

    # Loop through all students and check if they are enrolled in the course
    for i in range(len(ids)):
        if course == class1[i].lower() or course == class2[i].lower() or course == class3[i].lower():
            found_class.append((ids[i], first_names[i], last_names[i]))

    # If any students were found, display their information
    if found_class:
        print(f"Students enrolled in {course.capitalize()}:")
        for student in found_class:
            print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}")
    else:
        print(f"No students found for course: {course.capitalize()}")

# Part 4: Binary Search Function for IDs and Last Names
# Binary search is used for efficient searching through sorted lists.
# The function returns the index of the item if found, or -1 if not found.
def binary_search(search_list, target):
    low = 0
    high = len(search_list) - 1
    target = target.lower()  # Convert target to lowercase for case-insensitive search

    while low <= high:
        mid = (low + high) // 2
        if search_list[mid].lower() == target:
            return mid  # Found, return the index
        elif search_list[mid].lower() < target:
            low = mid + 1  # Search in the upper half
        else:
            high = mid - 1  # Search in the lower half
    return -1  # Not found

# Function to search for a student by ID using binary search
def search_by_id():
    search_id = input("Enter student ID: ")
    index = binary_search(ids, search_id)
    if index != -1:
        # If found, display the full student record
        print(f"ID: {ids[index]}, Last Name: {last_names[index]}, First Name: {first_names[index]}, Classes: {class1[index]}, {class2[index]}, {class3[index]}")
    else:
        print(f"Student with ID {search_id} not found.")

# Function to search for a student by last name using binary search
def search_by_last_name():
    search_name = input("Enter student's last name: ")
    index = binary_search(last_names, search_name)
    if index != -1:
        # If found, display the full student record
        print(f"ID: {ids[index]}, Last Name: {last_names[index]}, First Name: {first_names[index]}, Classes: {class1[index]}, {class2[index]}, {class3[index]}")
    else:
        print(f"Student with last name {search_name} not found.")

# Part 5: Main Program Loop
# This loop repeatedly shows the menu and processes the user's choice.
# The program will continue running until the user chooses to exit.
def main():
    while True:
        choice = display_menu()  # Show the menu and get the user's choice
        
        if choice == '1':
            # Option 1: Display all student data stored in the lists
            for i in range(len(ids)):
                print(f"ID: {ids[i]}, Last Name: {last_names[i]}, First Name: {first_names[i]}, Classes: {class1[i]}, {class2[i]}, {class3[i]}")
        
        elif choice == '2':
            # Option 2: Search by student ID
            search_by_id()
        
        elif choice == '3':
            # Option 3: Search by last name
            search_by_last_name()
        
        elif choice == '4':
            # Option 4: View a class roster by entering the class name
            course = input("Enter the class name: ")
            sequential_search(course)
        
        elif choice == '5':
            # Option 5: Exit the program
            print("Goodbye!")
            break  # Exit the loop to end the program
        
        else:
            # Invalid choice handling
            print("Invalid choice, please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
