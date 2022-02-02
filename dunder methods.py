class Employee : 
    increment = 1.5 
    no_of_employees = 0 
    def __init__(self,fname,lname,salary):
        self.fname = fname 
        self.lname = lname 
        self.salary = salary
        Employee.no_of_employees += 1 

    def __add__(self,other):   # Dunder method it returns salaries of both instances 
        return self.salary + other.salary
    
    def __repr__(self):     # It will return instance 
        return "Employee({},{},{})".format(self.fname,self.lname,self.salary)
    
    def __str__(self):
        return "Name of the Employee is {}".format(self.fname)


emp1 = Employee('harry','jackson',454)
emp2 = Employee('Jackie','chang',35353)


#With dunder methods 

print(emp1 + emp2)
print(repr(emp1))
print(str(emp1))


#without dunder method
print(emp1 + emp2) # it will give TypeError
print(repr(emp1))   # it gives address of emp1 
print(str(emp1))    # it also gives address of emp1 
