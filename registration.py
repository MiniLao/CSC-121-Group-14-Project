#
# Group 14 Project
# Cyndi Rathavongsa, Yair Rayo, Sylvia Ogunjobi
# Class Registration System
#

# Define data structures
student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444'), ('1005', '555'), ('1006', '666')]
student_in_state = {'1001': True, '1002': False, '1003': True, '1004': False, '1005': False, '1006': True}
course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3, 'CSC105': 2}
course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': [], 'CSC105': ['1005', '1002']}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3, 'CSC105': 4}

# Var
add_class = ()

# Function to log in a student
def login(id, s_list):
    pin = input("Enter your PIN: ")
    for student_id, student_pin in s_list:
        if id == student_id and pin == student_pin:
            print("ID and PIN verified.\n")
            return True
    print("ID and PIN incorrect.\n")
    return False

# Function to display the action menu
def show_menu():
    print("----------------")
    print("1. Add courses")
    print("2. Drop courses")
    print("3. List courses")
    print("4. Show bill")
    print("0. Log out")

# Function to manage the registration system
def main():
    while True:
        student_id = input("Enter ID to log in, or 0 to quit: ")
        if login(student_id, student_list):
            print("Action Menu")
            while True:
                show_menu()
                choice = input("What do you want to do? ")
                if choice == "1":
                    add_class = input("Enter course you want to add: ")

                elif choice == "2":
                    print("Enter course you want to drop: ")

      ######

                #elif choice == "3":
                    #print()
                #elif choice == "4":
                    # Implement displaying a bill logic here
                    #pass
                #elif choice == "0":
                    #print("Logging out.")
                    #break
                #else:
                    #print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()





