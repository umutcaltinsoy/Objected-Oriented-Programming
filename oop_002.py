#Class Variables

class Employee:

    num_of_emps  = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

print(Employee.num_of_emps) #it'll give us 0. because we haven't created employees yet.
emp_1 = Employee('Umut', 'Cagri', 1000)
emp_2 = Employee('Test', 'User', 2000)
print(Employee.num_of_emps)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__) # we can access values for emp_1. Except raise_amount

Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
