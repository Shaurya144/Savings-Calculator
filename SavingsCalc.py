# First we need to ask  how much they get per week
Weekly_Money = int(input("How much pocket money do you get per week? "))

# Now we need to find out how much they spend per weeek
Weekly_Spend = int(input("How much do you spend in a week? "))

# Finally, we can work out how much they have left (their savings), this is how much they can save in a week
Weekly_Savings = Weekly_Money - Weekly_Spend
Yearly_Savings = Weekly_Savings * 52 # This is how much they can save in a year (annually)

print("Therefore you can save " + str(Weekly_Savings) + " per week.")
print("Additionaly, you can save " + str(Yearly_Savings) +  " in a year.")
