#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to your personal tip calculator!")
bill_total = input("What was the total bill amount? $")
tip_percentage = input("What percentage of tip would you like to leave your server? ")
group_size = input("How many persons in your group today? ")

bt = float(bill_total)
tp = float(tip_percentage)/100
gs = int(group_size)

# ind_payment = "%0.2f" %(round((bt * (1 + tp) / gs),2))
ind_payment = "{:.2f}".format(round((bt * (1 + tp) / gs),2))

print(f"Each person should pay: ${ind_payment}")