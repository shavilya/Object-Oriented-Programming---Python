class Employee : 
    def __init__(self,fname,lname,salary):
        self.fname = fname 
        self.lname = lname 
        self.salary = salary



employee1 = Employee('harry','jackson',6565)
employee2 = Employee('Kaira','Adwani',5343)
print("Name of emp is {} {} and his/her salary is {} rs".format(employee1.fname,
employee1.lname,employee1.salary))
print("Name of emp is {} {} and his/her salary is {} rs".format(employee2.fname,
employee2.lname,employee2.salary))
