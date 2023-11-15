# Student Name: Sylvia Ogunjobi
# Billing program

# This program is a function file which is called by the main program which is registration.py

# This is the billing part of a complete student class registration system, this part calculates the student bill
# for the number of credit hours the student have selected, for in-state student the price of each credit hour is
# $225, and  the price of each credit hour for out-state students is $850. The program will calculate the bill
# according to the number of credit hours selected by the student.

import datetime


def display_bill(s_id, s_in_state, c_rosters, c_hours):
    # The below code will check the current status of the student whether
    # it is out-state student or in-state student
    in_state = s_in_state.get(s_id, False)

    # The below code will calculate the cost of per credit hour based on in-state and out-state condition
    if in_state:
        crdt_hr_fee = 225  # Per credit hour fee for in-state students
    else:
        crdt_hr_fee = 850  # Per credit hour fee for out-state students

    # The below line will update the current date and time on every iteration
    current_datetime = datetime.datetime.now()

    # The below code will display the tuition fee summary
    print("\n Tuition Summary")
    print(f"Student: {s_id}, {'In-State' if in_state else 'Out-of-State'} Student")
    print(current_datetime.strftime("%b %d, %Y at %I:%M %p"))
    print("{:<10} {:<7} {:<10}".format("Course", "Hours", "Cost"))
    print("-" * 30)

    total_cost = 0

    # The below code will calculate the cost for each selected course, every time the loop runs
    for course, hours in c_hours.items():

        # The below code will check if previously student was enrolled in that course or not
        if s_id in c_rosters.get(course, []):
            cost = hours * crdt_hr_fee
            total_cost += cost
            print("{:<10} {:<7} ${:,.2f}".format(course, hours, cost))

    # The below line will display the final amount of the bill the student have to pay
    print("{:<20} {:<7} ${:,.2f}".format("Total", sum(c_hours.values()), total_cost))
