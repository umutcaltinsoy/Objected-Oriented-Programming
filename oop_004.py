#Inheritance: Creating Subclasses

class Employee:

    raise_amt= 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee): #We want to inherit from Employee class
    #If we wanted our developers to have a raise amount of %10
    raise_amt = 1.10
    '''
    Because, we inherit raise amount from Employee Class
    Changing the raise amount in our subclass, it didn't
    affect on any of our employee insances so they still
    have that raise amountof %4. So we can make these
    changes to out subclasses without worryin about breaking
    anything in the parent class
    '''

#And now we'll make a few more complicated changes

    def __init__(self, first, last, pay, prog_lang):

        #self.first = first
        #self.last = last
        #self.pay = pay
        #self.email = first + '.' + last + '@company.com'
        #Instead of copy this code we use super() method
        super().__init__(first, last, pay)
        #super() method doesn't accept any arguments 'self'
        #And also we can use instead of super() method -> Employee._init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Umut', 'Cagri', 10000, 'Python')
dev_2 = Developer('Test', 'User', 20000, 'Java')

mgr_1 = Manager('Jürgen', 'Klopp', 30000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
#mgr_1.remove_emp(dev_1)
#mgr_1.print_emps()

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_1.prog_lang)


#Pyton has these two builtin functions called isinstance() and issubclass() :
print(isinstance(mgr_1, Employee)) #Check: mgr_1 is an instance of; Employee = True, Maneger = True, Developer = False
print(issubclass(Manager,Employee)) #It'll tell us if a class is a subclass of another

