def salary_hike(s,hike):
    salary_hike=s+(s*hike/100)
    return salary_hike

salary=int(input("Enter old salary:"))
hike=int(input("Enter hike:"))
new_salary=salary_hike(salary,hike)
print("New salary:",new_salary)