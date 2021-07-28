#Class methods and static methods

class Employee:

    num_of_emps = 0
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

    @classmethod #classmethod decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Umut', 'Cagri', 10000)
emp_2 = Employee('Test', 'User', 20000)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

emp_str_1 = 'John-Wick-10000'
emp_str_2 = 'Steve-Jobs-20000'
emp_str_3 = 'Jack-Jones-30000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

