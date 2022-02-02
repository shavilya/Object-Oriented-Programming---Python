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
    def from_str(cls,emp_string):
        fname , lname , salary = emp_string.split('-')
        return cls(fname,lname,salary)

    @staticmethod 
    def isopen(day):
        if day == 'sunday':
            return False 
        else : 
            return True 

class Programmer(Employee):                               #child class - inheritance
    def __init__(self,fname,lname,salary,prglang,exp):
        super().__init__(fname,lname,salary)              # it calls Employee class constructor.
        self.prglang = prglang 
        self.exp = exp 
        self.increment = 2.5
    
    def salary_increase(self):
        self.salary = int(self.salary * self.increment)

emp1 = Employee('harry','jackson',454)
emp2 = Employee.from_str('Jackie-chang-4343')

emp3 = Programmer('john','stelwart',45454,'python','5 yrs')

"""print(emp1.salary)
emp1.change_increment(2)
emp1.increase()
print(emp1.salary)
print(emp2.fname)
print(Employee.isopen('monday'))"""

print(emp3.exp)
emp3.salary_increase()
print(emp3.salary)
