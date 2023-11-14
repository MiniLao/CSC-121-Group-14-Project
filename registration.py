#
# Group 14 Project
# Cyndi Rathavongsa, Yair Rayo, Sylvia Ogunjobi
# Class Registration System
#

from student import add_course
from student import drop_course
from student import list_courses
from billing import display_bill

# Define data structures
student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]
student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}
course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

# Var
add_class = ()

# ------------------------------------------------------------
# This function allows a student to log in.
# It has two parameters: s_id and s_list, which is the student
# list. This function asks user to enter PIN. If the ID and PIN
# combination is in s_list, display message of verification and
# return True. Otherwise, display error message and return False.
# -------------------------------------------------------------
def login(id, s_list):
    pin = input("Enter your PIN: ")
    for student_id, student_pin in s_list:
        if id == student_id and pin == student_pin:
            print("ID and PIN verified.\n")
            return True
    print("ID and PIN incorrect.\n")
    return False

# ------------------------------------------------------------
# This function displays the action menu to the logged in student.
# It takes no parameters and returns no values.
# -------------------------------------------------------------
def show_menu():
    print("----------------")
    print("1. Add courses")
    print("2. Drop courses")
    print("3. List courses")
    print("4. Show bill")
    print("0. Log out")


# ------------------------------------------------------------
# This function manages the whole registration system.  It has
# no parameter.  It creates student list, in_state_list, course
# list, max class size list and roster list.  It uses a loop to
# serve multiple students. Inside the loop, ask student to enter
# ID, and call the login function to verify student's identity.
# Then let student choose to add course, drop course or list
# courses. This function has no return value.
# -------------------------------------------------------------
def main():
    while True:
        student_id = input("Enter ID to log in, or 0 to quit: ")
        if login(student_id, student_list):
            print("Action Menu")
            while True:
                show_menu()
                choice = input("What do you want to do? ")
                if choice == "1":
                    add_course(student_id, course_roster, course_max_size)

                elif choice == "2":
                    drop_course(student_id, course_roster)

                elif choice == "3":
                    list_courses(student_id, course_roster)

                elif choice == "4":
                    display_bill(id, student_in_state, course_roster, course_hours)

                elif choice == "0":
                    print("Session ended.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()





