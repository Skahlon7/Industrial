def Trip_miles(city):
    if  city == "Sacramento":
        destination = 45
        tax = .146
        hours = (destination*1.35)/60  #1.35 = median duration of time per mile from data set of 70 drivers at KPI Logistics (Room for increased accuracy)
        salary = hours*27.15
        true_salary = salary - (salary*tax)
    elif city == "Seattle":
         destination = 742
         tax = .146
         hours = (destination*1.35)/60
         salary = hours*27.15
         true_salary = salary - (salary*tax)
    elif city == "Chicago":
         destination = 988
         tax = .146
         hours = (destination*1.35)/60
         salary = hours*27.15
         true_salary = salary - (salary*tax)
    elif city == "Los Angeles":
        destination = 408
        tax = .146
        hours = (destination*1.35)/60
        salary = hours*27.15
        true_salary = salary - (salary*tax)
    elif city == "Manhattan":
        destination = 2483
        tax = .1876
        hours = (destination*1.35)/60
        salary = hours*27.15
        true_salary = salary - (salary*tax)
    elif city == "Miami":
        destination = 2539
        tax = .146
        hours = (destination*1.35)/60
        salary = hours*27.15
        true_salary = salary - (salary*tax)
    elif city == "Miluakee":
        destination = 1754
        tax = .146
        hours = (destination*1.35)/60
        salary = hours*27.15
        true_salary = salary - (salary*tax)
    elif city == "Houston":
        destination = 1954
        tax = .146
        hours = (destination*1.35)/60
        salary = hours*27.15
        true_salary = salary - (salary*tax)
    else:
        destination = "not supported by KPI Logistics LLC. KPI Logistics is an industry leader in commercial and private transportation with a shipping range of 3,500" 
        hours = " We offer employee benefits, medicare, five weeks of vacation, and flexible "
        true_salary = "27.15 an hour, KPI Logistics is recognized and rewarded by several Union and government organization as a labor rights champion. KPI Logistics LLC is an equal opportunity employer. Contact (916)-412-1139. KPI Logistics LLC, Roseville, California, 95677."
    return "The destination is " + str(destination) + " miles. " + str(hours) + " hours. Paying $" + str(true_salary)
