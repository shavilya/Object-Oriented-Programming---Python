class Employee : 
    def __init__(self,fname,lname,salary):
        self.fname = fname 
        self.lname = lname 
        self.salary = salary 
        
    @property
    def email(self):
        return self.fname + '.' + self.lname + '@gmail.com'

    @email.setter
    def email(self,given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]
         

if __name__ == '__main__':
    Emp1 = Employee('harry','jackson',124124)
    Emp2 = Employee('katrina','kaif',45343)

    print(Emp1.email , Emp2.email)
    Emp1.lname = 'khanna'
    print(Emp1.email)
    Emp2.email = 'kaif.katrina@gmail.com'
    print(Emp2.email)

    