class Employee :
    increment = 1.5 
    no_of_employees = 0 
    def __init__(self,fname,lname,salary):
        self.fname = fname 
        self.lname = lname 
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls,amount): 
        cls.increment = amount

    @classmethod
    def from_str(cls , emp_string):
        fname,lname,salary = emp_string.split('-')
        return cls(fname,lname,salary) 


emp1 = Employee('harry','code',5345343)
emp2 = Employee('kaira','adwani',463463)
emp3 = Employee.from_str('katrina-kaif-5744475')

print(Employee.no_of_employees)
print("Starting salary of emp1 is : " + str(emp1.salary))
emp1.change_increment(2)
emp1.increase()
print("After 1st promotion emp1's salary becomes : " + str(emp1.salary))
print("another employee is {} {}".format(emp3.fname,emp3.lname))
print("Total number of employees in our firm : " , str(Employee.no_of_employees))