#
# Group 14 Project
# Main Author: Yair Rayo
# Cyndi Rathavongsa, Yair Rayo, Sylvia Ogunjobi
# Class Registration System
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. Relied on pseudocode to determine steps.
# -----------------------------------------------------------------

def list_courses(s_id, c_roster):
    # ------------------------------------------------------------
    # This function displays all the courses, indicates which ones
    # in which the student is enrolled, and counts the courses a
    # student has registered for. It has two parameters: s_id is the
    # ID of the student; c_roster is the list of class rosters.
    # This function has no return value.
    # -------------------------------------------------------------

    # Initializing an empty list named 'courses_registered' for later use.
    courses_registered = []

    # Display a header titled 'Courses' for a list of registered courses. This gives the user context on what
    # information will be displayed below this label.
    print('Courses: ')

    # This 'for loop' will display the enrolled message
    for course, roster in c_roster.items():
        if s_id in roster:
            print(course, 'Enrolled')
            courses_registered.append(course)
        else:
            print(course)

    # Finally, if no error encountered, display total enrolled courses, one by one.
    print('Total courses enrolled: ', len(courses_registered))


def add_course(s_id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: s_id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    # Ask user which classe they want to add and save input to 'new_added_course'.
    new_added_course = input('Enter the course you want to add: ')

    # First, 'if' statement checks input and compares to available courses. If input does not match an existing
    # course, then print 'Course not found'. The 'return' statement stops, and exits the function.
    if new_added_course not in c_roster:
        print(f'Error: Course {new_added_course} not found.')  # Used f string to display their input in error message.
        return  # Exit function here.

    # Next, check if student is already registered to the desired course by looking through the student id and course
    # roster.
    if s_id in c_roster[new_added_course]:
        print(f'Error: You are already registered for course {new_added_course}')  # Display error message
        return  # Exit function here

    # Next, check if desired course is full based on the c_max_size parameter with 'if'. If the course is full,
    # display error message and return.
    if len(c_roster[new_added_course]) >= c_max_size[new_added_course]:
        print(f'Error: Course {new_added_course} already full.')
        return  # Exit function here

    # Finally, if all error conditions are avoided, add the student ID to the course’s roster and display a message.
    c_roster[new_added_course].append(s_id)
    print(f'Course {new_added_course} added.')


def drop_course(s_id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: s_id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------

    # Ask user which classe they want to add and save input to 'course_to_drop'.
    course_to_drop = input('Enter the course you want to drop: ')

    # First, 'if' statement checks input and checks if the course exist in roster.
    if course_to_drop not in c_roster:
        print(f'Error: You are not enrolled in course {course_to_drop}.')  # If the course not offered, display error.
        return  # Exit function here

    # Next, check if student is not enrolled in desired class to drop. If not, display error message.
    if s_id not in c_roster[course_to_drop]:
        print(f'Error: You are not enrolled in course {course_to_drop}.')
        return  # Exit function here

    # Finally, if no error encountered remove student id from roster and display confirmation message.
    c_roster[course_to_drop].remove(s_id)
    print(f'Course {course_to_drop} dropped.')
