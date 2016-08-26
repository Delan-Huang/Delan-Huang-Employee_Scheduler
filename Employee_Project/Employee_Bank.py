class Employee:
    def __init__(self, name, job, availability):
        self.name = name
        self.job = job
        self.availability = availability  # number of shifts per week

        self.still_available = True
        self.days_assigned_month = []
        self.days_assigned_week = []

    def assignDay(self, date):
        "Date must be in 'mm/dd' format"
        self.days_assigned_week.append(date)
        self.days_assigned_month.append(date)

    def clearDaysAssignedWeek(self):
        self.days_assigned_week = []

    def clearDaysAssignedMonth(self):
        self.days_assigned_month = []

    def getAssignedDaysMonth(self):
        return self.days_assigned_month

    def getAssignedDaysWeek(self):
        return self.days_assigned_week

    def checkAvailability(self):
        if len(self.days_assigned_week) == self.availability:
            self.still_available = False
        else:
            self.still_available = True


Analisa = Employee("Analisa", "PIC2", 2)
NaNa = Employee("Nana", "PIC1+", 2)
Cisco = Employee("Cisco", "PIC2", 2)
Kristie = Employee("Kristie", "PIC1+", 1)
Denise = Employee("Denise", "PIC1+", 2)
Mai = Employee("Mai", "PIC1", 1)
Karen = Employee("Karen", "PIC1", 2)
Diane = Employee("Diane", "PIC2", 2)
Tarai = Employee("Tarai", "PIC1", 2)
Cory = Employee("Cory", "PIC2", 1)
Viet = Employee("Viet", "PIC2", 1)
Rachel_Mariah = Employee("Rachel_Mariah", "PIC1", 1)

employee_bank = [Mai, Karen, Tarai, Rachel_Mariah, NaNa, Denise, Kristie, Analisa, Cisco, Diane, Cory, Viet]
PIC1_Employees = [Mai, Karen, Tarai, Rachel_Mariah]
PIC1P_Employees = [NaNa, Denise, Kristie]
PIC2_Employees = [Analisa, Cisco, Diane, Cory, Viet]
