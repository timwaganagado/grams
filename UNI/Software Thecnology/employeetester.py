import employee as E

def createListOfEmployee():
    resume = True
    staff = []
    sal = 0
    while resume:
        name = input("Enter Staff member's name: ")
        howpay = input("Enter staff's classification (Salaried or Hourly): ")
        if howpay == "Salaried":
            a = E.SalariedEmployee()
            sal += 1
        else:
            a = E.HourlyEmployee()
        a.setName(name)
        a.setHoursWorked(input("Enter the number of hours worked: "))
        if howpay == "Salaried":
            a.setRate(input("Enter weekly salary: "))
        else:
            a.setRate(input("Enter hourly wage: "))
        staff.append(a)
        resume = input("Do you want to continue (Y/N)? ")
        if resume == "N":
            resume = False
    return staff,sal

def displayResults(staff,sal):
    totpay = 0
    tothours = 0
    totstaff = len(staff)
    for x in staff:
        pay = x.calculatePay()
        print(f"{x.getName()}: ${pay:,}")
        tothours += x.getHoursWorked()
        totpay += pay
    print(f"Number of staff members: {totstaff}")
    print(f"Number of salaried staff: {sal}")
    print(f"Total payroll: ${totpay:,}")
    print(f"Average number of hours worked per staff member: {tothours/totstaff}")
    
def main():
    print("===Staff Payroll System===")
    staff,sal = createListOfEmployee()
    displayResults(staff,sal)

if __name__ == "__main__":
    main()