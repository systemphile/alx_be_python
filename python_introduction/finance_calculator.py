#Python script to find user’s monthly savings and potential future savings
income = float(input("Enter your monthly income: \n")) #user provides monthly income
expenses = float(input("Enter your total monthly expenses: \n")) #user provides monthly expenses
savings = income - expenses #caculate the monthly savings
projected_savings = savings * 12 + (savings * 12 * 0.05) #calculate the projected savings

#print savings
print (f"Your monthly savings are {savings}\nProjected savings after one year, with interest, is: {projected_savings}")