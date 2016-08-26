import Employee_Algorithm_Sim_20160807
from Employee_Bank import *
import Monthly_Calendar

monthly_calendar = Monthly_Calendar.create_monthly_calendar(2016, 9)

for i in range(1):
    random_solution = Employee_Algorithm_Sim_20160807.create_solution(employee_bank, monthly_calendar)
    print random_solution

# random_solution = Employee_Algorithm_Sim.create_solution(employee_bank, monthly_calendar)

# print "-"*15, "Random Solution", "-"*15, "\n"
# print "Days: ", monthly_calendar
# print "Num weeks: ", len(monthly_calendar)
# print "\n"
#
# print "-"*15, "Random Solution", "-"*15, "\n"
# print random_solution, "\n"
