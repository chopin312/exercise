#significant constant
tax_rate =  0.2
standard_deduction = 10000
deductuion_per_dependent = 4500
#inputs
gross_income = float(input("Please,put your income "))
number_of_dependent = float(input("How many times do you hangout "))
#calculate
net_income = gross_income - standard_deduction - deductuion_per_dependent * number_of_dependent
income_tax = net_income * tax_rate
#output
print("Your income before calculate the tax is " + str(round(net_income, 2)))
print("And if we calculate your income tax with your net income  " + str(round(income_tax, 2)))
print("So your income contains  " + str(round(net_income-income_tax, 2)))
