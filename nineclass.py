class working:
    company = "Microsoft"
     
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getinfo(self):
        print("Company:", self.company)
        print("Name:", self.name)
        print("Salary:", self.salary)

employee1 = working("Manoj", 180000)
print(employee1.name, employee1.salary, employee1.company)

employee2 = working("Ravi", 150000)
print(employee2.name, employee2.salary, employee2.company)
