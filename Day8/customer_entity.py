class Customers:
    def __init__(self, customerId, name, age, gender):
        self.customerId = customerId
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        customer = 'Customers(' + self.customerId + ',' + self.name + ',' + self.age + ',' + self.gender + ')'
