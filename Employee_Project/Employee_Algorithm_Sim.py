import numpy as np
import Employee_Bank as eb

# Global Constant
E = 2.71828


def create_solution(employee_bank, month_calendar):
    """Create a random (but correct) solution. Requires:
    - Employee Bank
    - Month separated by work weeks/days with markers"""

    leftover_employees = []

    # Per Week
    for weeks in xrange(len(month_calendar)):
        # Per Day

        # Make sure employee banks are populated
        remain_PIC1 = eb.PIC1_Employees[:]
        remain_PIC1P = eb.PIC1P_Employees[:]
        remain_PIC2 = eb.PIC2_Employees[:]

        for days in xrange(len(month_calendar[0])):
            # Create Date
            date = "/".join(month_calendar[weeks][days])

            # needed to reset while loops
            assigned_PIC1 = False
            assigned_PIC1P = False
            assigned_PIC2 = False

            # randomly assign PIC1 employees to start
            while not assigned_PIC1:
                # Create weights for random employee selections
                all_banks_weight = []
                ab_pic1_weight = 0.80
                ab_pic1p_weight = 0.10
                ab_pic2_weight = 0.10

                print "Length of PIC1 (before first loop): ", len(remain_PIC1)
                print "Length of PIC1P (before first loop): ", len(remain_PIC1P)
                print "Length of PIC2 (before first loop): ", len(remain_PIC2)
                print "remaining: ", len(remain_PIC1 + remain_PIC1P + remain_PIC2)

                # weights for all_banks_weight
                try:
                    ab_pic1 = ab_pic1_weight / len(remain_PIC1)
                except ZeroDivisionError:
                    ab_pic1 = 0.0
                    ab_pic1_weight = 0.0
                try:
                    ab_pic1p = (1.0 - ab_pic1_weight - ab_pic2_weight) / len(remain_PIC1P)
                    ab_pic1p_weight = 1.0 - ab_pic1_weight - ab_pic2_weight
                except ZeroDivisionError:
                    ab_pic1p = 0.0
                    ab_pic1p_weight = 0.0
                try:
                    ab_pic2 = (1.0 - ab_pic1_weight - ab_pic1p_weight) / len(remain_PIC2)
                    ab_pic2_weight = 1.0 - ab_pic1_weight - ab_pic1p_weight
                except ZeroDivisionError:
                    ab_pic2 = 0.0
                    ab_pic2_weight = 0.0

                # Assign weights
                for employee in remain_PIC1 + remain_PIC1P + remain_PIC2:
                    if employee.job == "PIC1":
                        all_banks_weight.append(ab_pic1)
                    elif employee.job == "PIC1+":
                        all_banks_weight.append(ab_pic1p)
                    else:
                        all_banks_weight.append(ab_pic2)

                print "all_banks_weight: ", all_banks_weight

                PIC1 = np.random.choice(remain_PIC1 + remain_PIC1P + remain_PIC2, p=all_banks_weight)

                # Basic Employee Info
                # print PIC1.name, PIC1.job, PIC1.getAssignedDaysMonth()

                # Check Availability before assigning day
                PIC1.checkAvailability()
                if PIC1.still_available:
                    PIC1.assignDay(date)
                    assigned_PIC1 = True
                else:
                    if PIC1.job == "PIC1":
                        remain_PIC1.remove(PIC1)
                    elif PIC1.job == "PIC1+":
                        remain_PIC1P.remove(PIC1)
                    else:
                        remain_PIC2.remove(PIC1)

                        # print all_banks_weight

            # randomly assign PIC1+ employees to supplement
            while not assigned_PIC1P:
                # Create weights for PIC1p_PIC2
                PIC1P_PIC2_weight = []
                both_pic1p_weight = 0.65
                both_pic2_weight = 0.35

                print "Length of PIC1 (before second loop): ", len(remain_PIC1)
                print "Length of PIC1P (before second loop): ", len(remain_PIC1P)
                print "Length of PIC2 (before second loop): ", len(remain_PIC2)
                print "remaining: ", len(remain_PIC1P + remain_PIC2)

                # weights for PIC1_PIC2
                try:
                    both_pic1p = (1.0 - both_pic2_weight) / len(remain_PIC1P)
                except ZeroDivisionError:
                    both_pic1p = 0.0  # clears weight values for PIC1P and allows program to grab from PIC2
                    both_pic1p_weight = 0.0

                try:
                    both_pic2 = (1.0 - both_pic1p_weight) / len(remain_PIC2)
                except ZeroDivisionError:
                    both_pic2 = 0.0
                    try:
                        both_pic1p = 1.0 / len(remain_PIC1P)  # remove PIC2 weight values and grab from PIC1P
                    except ZeroDivisionError:
                        both_pic1p = 0.0

                # Assign weights
                for employee in remain_PIC1P + remain_PIC2:
                    if employee.job == "PIC1+":
                        PIC1P_PIC2_weight.append(both_pic1p)
                    if employee.job == "PIC2":
                        PIC1P_PIC2_weight.append(both_pic2)

                print "PIC1_PIC2: ", PIC1P_PIC2_weight

                PIC1P = np.random.choice(remain_PIC1P + remain_PIC2, p=PIC1P_PIC2_weight)

                # Basic Employee Info
                # print PIC1P.name, PIC1P.job, PIC1P.availability, PIC1P.still_available

                # Check Availability before assigning day
                PIC1P.checkAvailability()
                if PIC1P.still_available:
                    PIC1P.assignDay(date)
                    assigned_PIC1P = True
                else:
                    if PIC1P.job == "PIC1+":
                        remain_PIC1P.remove(PIC1P)
                    if PIC1P.job == "PIC2":
                        remain_PIC2.remove(PIC1P)

            # randomly assign PIC2 employees to fill out leftover spots
            while not assigned_PIC2:
                PIC2 = np.random.choice(remain_PIC2)  # Basic Employee Info

                # print PIC2.name, PIC2.job, PIC2.availability, PIC2.still_available

                # Check Availability before assigning day
                PIC2.checkAvailability()
                if PIC2.still_available:
                    PIC2.assignDay(date)
                    assigned_PIC2 = True
                else:
                    remain_PIC2.remove(PIC2)

        # Keep a list of leftover employees (later may want to prefer these employees)
        temp_leftover_employees = []
        for employee in employee_bank:
            if len(employee.getAssignedDaysWeek()) <= 1:
                temp_leftover_employees.append([employee.name, 2 - len(employee.getAssignedDaysWeek())])

        leftover_employees.append(temp_leftover_employees)

        # Print statements to keep track week by week
        temp_scheduled_employees = []
        for employee in employee_bank:
            temp = employee.name, employee.getAssignedDaysWeek()
            temp_scheduled_employees.append(temp)

        # print "-" * 15, "Employee Schedule for week: %i" % weeks, "-" * 15
        # print temp_scheduled_employees, "\n"
        # print "-" * 15, "Extra Employee Shifts for week: %i" % weeks, "-" * 15
        # print temp_leftover_employees, "\n"

        # Clear assigned days in week for next week
        for employee in employee_bank:
            employee.clearDaysAssignedWeek()

    # Jobs assigned to all employees
    assigned_jobs_monthly = []
    for employee in employee_bank:
        employee_schedule = [employee.name, employee.getAssignedDaysMonth()]
        assigned_jobs_monthly.append(employee_schedule)

    # Jobs assigned to PIC1
    assigned_jobs_PIC1 = []
    for employee in eb.PIC1_Employees:
        employee_schedule = [employee.name, employee.getAssignedDaysMonth()]
        assigned_jobs_PIC1.append(employee_schedule)

    # Jobs assigned to PIC1P
    assigned_jobs_PIC1P = []
    for employee in eb.PIC1P_Employees:
        employee_schedule = [employee.name, employee.getAssignedDaysMonth()]
        assigned_jobs_PIC1P.append(employee_schedule)

    # Jobs assigned to PIC2
    assigned_jobs_PIC2 = []
    for employee in eb.PIC2_Employees:
        employee_schedule = [employee.name, employee.getAssignedDaysMonth()]
        assigned_jobs_PIC2.append(employee_schedule)

    # print assigned_jobs_PIC1
    # print assigned_jobs_PIC1P
    # print assigned_jobs_PIC2
    # print leftover_employees

    # return solution
    return assigned_jobs_monthly


def score(solution):
    """Calculates the score of a solution based on the following restrictions:
        SOFT RESTRICTIONS
        - Prefer to spread out shifts evenly
        - """

    return score


def acceptance_probability(old_score, new_score, temp):
    """Calculates Acceptance Probability (ap)"""
    ap = E ** ((old_score - new_score) / temp)
    return ap


def anneal(employee_bank, month_calendar):
    old_solution = create_solution(employee_bank, month_calendar)
    old_score = score(old_solution)
    temp = 1.0
    temp_min = 0.00001
    alpha = 0.9
    while temp > temp_min:
        i = 1
        while i <= 100:
            new_solution = create_solution(employee_bank, month_calendar)
            new_score = score(new_solution)
            ap = acceptance_probability(old_score, new_score, temp)
            if ap > np.random.random():
                old_solution = new_solution
                old_score = new_score
            i += 1
        temp = temp * alpha
    return old_solution, old_score
