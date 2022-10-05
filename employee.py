"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary = 0, hourly_wage = 0, contract_hours = 0, contracts_landed = 0, bonus_commission = 0, contract_commission = 0):
        self.name = name
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.contract_hours = contract_hours
        self.contracts_landed = contracts_landed
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission


    def get_pay(self):
        total_pay = 0
        if self.salary > 0:
            total_pay += self.salary
        else:
            total_pay += (self.contract_hours * self.hourly_wage)
        if self.contracts_landed > 0:
            total_pay += (self.contracts_landed * self.contract_commission)
        if self.bonus_commission:
            total_pay += self.bonus_commission
        return total_pay

    def __str__(self):
        description = self.name
        if self.salary > 0:
            description += (" works on a monthly salary of " + str(self.salary))
            if self.bonus_commission > 0:
                description += (" and receives a bonus commission of " + str(self.bonus_commission) + ".")
            else:
                description += "."
        else:
            description += (" works on a contract of " + str(self.contract_hours) + " at " + str(self.hourly_wage))
            if self.contracts_landed > 0:
                description += (" and receives a commission for " + str(self.contracts_landed) + " contract(s) at " + str(self.contract_commission) + "/contract.")
            else:
                description += "."
        description += (" Their total pay is " + str(self.get_pay()) + ".")
        return description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract_hours = 100, hourly_wage = 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary = 3000, contracts_landed = 4, contract_commission = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract_hours = 150, hourly_wage = 25, contracts_landed = 3, contract_commission = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, bonus_commission = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract_hours = 120, hourly_wage = 30, bonus_commission = 600)

print(billie.get_pay())
print(charlie.get_pay())
print(renee.get_pay())
print(jan.get_pay())
print(robbie.get_pay())
print(ariel.get_pay())

print(billie)
