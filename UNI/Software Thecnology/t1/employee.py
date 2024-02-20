class Employee:
    def __init__(self):
        self.hoursWorked = 0
        self.name = 0
        self.rate = 0
    def getHoursWorked(self):
        return int(self.hoursWorked)
    def getName(self):
        return self.name
    def getRate(self):
        return int(self.rate)
    def setHoursWorked(self,hours):
        self.hoursWorked = hours
    def setName(self,name):
        self.name = name
    def setRate(self,rate):
        self.rate = rate

class HourlyEmployee(Employee):
    def calculatePay(self):
        return self.getHoursWorked() * self.getRate()

class SalariedEmployee(Employee):
    def calculatePay(self):
        return int(self.rate)