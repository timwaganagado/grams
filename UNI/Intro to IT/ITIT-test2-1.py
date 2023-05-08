

#getting inputs
under = True
while under:
    salary = input("Salary: ")
    try:
        salary = int(salary)
        under = False
    except:
        under = True
    
    
under = True
while under:
    years_on_job = input("Years on job: ")
    try:
        years_on_job = int(years_on_job)
        under = False
    except:
        under = True
    
#comparing inputs to cases | salary to 30000 and years on job to 2
if salary >= 30000:
    if years_on_job >= 2:
        print("You qualify for the loan.".format())
    else:
        print("You must have been on your current job for at least two years to qualify.".format())
else:
    print("You must earn at least 30,000 per year to qualify.".format())