class Employee : 
    increment = 1.5 
    no_of_employees = 0 
    def __init__(self,fname,lname,salary):
        self.fname = fname 
        self.lname = lname 
        self.salary = salary
        Employee.no_of_employees +=1 

    def increase(self):
        self.salary = int(self.salary * Employee.increment)
    
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount 

    @classmethod 
    def from_str(cls,emp_string):
        fname , lname , salary = emp_string.split('-')
        return cls(fname,lname,salary) 
    
    @staticmethod                        # if we want an independent function which 
    def isopen(day):                     # does not take class nor instance variables
        if day == 'sunday':              # then one must use static method 
            return False
        else :
            return True 

emp1 = Employee('harry','jackson',50)
emp2 = Employee('kaira' , 'adwani' , 10)
emp3 = Employee.from_str('katrina-kaif-30')


print(emp1.fname ,emp1.lname , emp1.salary)
print(emp2.fname ,emp2.lname , emp2.salary)
print(emp3.fname ,emp3.lname , emp3.salary)
print(Employee.isopen('sunday'))