#Special (Magic/Dunder[Double Underscores]) Methods:

#These special methods allow us to emulate some built-in behavior within Python
#And it's also how we implement operator overloading
#These special methods are always surrounded by double underscores(dunder)
#So a lot of people call the double underscores dunder

# def __repr__(self):
#    pass

# def __str__(self):
#    pass

#These two special methods allow us to change how our objects are printed and displayed

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    #if we wanted to add two employees together and have the result their combined salaries
    #we're going to have create __add__
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Umut', 'Cagri', 10000)
emp_2 = Employee('Test', 'User', 20000)

print(len(emp_1))
#print(len('test')) = print('test'.__len__())

print(emp_1 + emp_2) #it gives us combined salaries
#print(emp_1)

print(repr(emp_1))
print(str(emp_1))
#print(emp_1.__repr__())
#print(emp_1.__str__())

print(1+2)
print(int.__add__(1,2))
