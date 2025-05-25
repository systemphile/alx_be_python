#Python script to find user’s monthly savings and potential future savings
income = float(input("Enter your monthly income: ")) #user provides monthly income
expenses = float(input("Enter your total monthly expenses: ")) #user provides monthly expenses
monthly_savings = income - expenses #caculate the monthly savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #calculate the projected savings

#print savings
print (f"Your monthly savings are {monthly_savings}\nProjected savings after one year, with interest, is: {projected_savings}")