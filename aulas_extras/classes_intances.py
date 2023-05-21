class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_01 = Employee('Paulo', 'Vidal', 50000)
emp_02 = Employee('Mariana', 'Toledo', 70000)

print(emp_01.email.lower())
print(emp_01.fullname())
print(emp_02.fullname().upper())