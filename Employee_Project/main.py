import Employee_Algorithm_Sim
from Employee_Bank import employee_bank
import Monthly_Calendar


# Create a work week calendar for the current month
monthly_calendar = Monthly_Calendar.create_current_monthly_calendar()

# Run the anneal function on the random solution
best_solution, best_score = Employee_Algorithm_Sim.anneal(employee_bank, monthly_calendar)

# Print best solution and best score
print "-"*15, "Best Solution", "-"*15, "\n"
print best_solution
print "\n"

print "-"*15, "Best Score", "-"*15, "\n"
print best_score
print "\n"

# Export results to an excel spreadsheet
