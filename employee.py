
class employees:
    def __init__(self, name,family,personnelcode):
        self.name =name
        self.family =family
        self.personnelcode = personnelcode

    def information_display(self):
        print(f"Name: {self.name}")
        print(f"family: {self.family}")
        print(f"personnelcode: {self.personnelcode}")

class hourlyemployee(employees):
    def __init__(self, name, family, personnelcode, function_huors):
        super().__init__(name,family,personnelcode)
        self.function_hours =function_huors

    def information_display(self):
        super().information_display()
        print(f"function_hours:{self.function_hours}")

class employeesalary(employees):
    def __init__(self,name,family,personnelcode,salary):
        super().__init__(name,family,personnelcode)
        self.salary=salary
    
    def information_display(self):
        super().information_display()
        print(f"salary:{self.salary}")


employees_list = [
hourlyemployee("reza","saeedi",265433,function_huors=140),
employeesalary("hesam","ahmadi",345677,salary=8000000),
] 
   
for employees in employees_list:
    employees.information_display()     
    print("\n")