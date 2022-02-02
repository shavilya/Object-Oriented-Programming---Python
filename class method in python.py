class Employee :  # Class 
    increment = 1.5 
    no_of_employees = 0
    def __init__(self,fname,lname,salary):   # constructor 
        self.fname = fname 
        self.lname = lname 
        self.salary = salary
        Employee.no_of_employees += 1 
       
    def increase(self):     
        self.salary = int(self.salary * Employee.increment)
    
    @classmethod        # Decorator 
    def change_increment(cls,amount):        # Here we are trying to change increment using decorator
        cls.increment= amount 
      
employee1 = Employee('harry','jackson',6565)
employee2 = Employee('Kaira','Adwani',5343)

print(employee1.salary)
Employee.change_increment(4)
employee1.increase()
print(employee1.salary)