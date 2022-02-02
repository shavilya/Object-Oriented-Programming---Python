# This code prints fname , lname and salary of employees and prints incremented salaries too 
# also it prints no of employee's created 

class Employee :  # Class 
    increment = 1.5 
    no_of_employees = 0
    def __init__(self,fname,lname,salary):   # constructor 
        self.fname = fname 
        self.lname = lname 
        self.salary = salary
        Employee.no_of_employees += 1 
       

    def increase(self):     
        return int(self.salary * Employee.increment)

employee1 = Employee('harry','jackson',6565)
employee2 = Employee('Kaira','Adwani',5343)
# print("Name of emp is {} {} and his/her salary is {} rs".format(employee1.fname,
# employee1.lname,employee1.salary))
# print("Name of emp is {} {} and his/her salary is {} rs".format(employee2.fname,
# employee2.lname,employee2.salary))

"""print(employee1.salary)
print(employee1.increase())"""


print(Employee.__dict__)  # gives all the objects of employee class
print(employee1.__dict__) # gives all the objects of employee1 object . 

print(Employee.no_of_employees)   # gives how many employees where created . 