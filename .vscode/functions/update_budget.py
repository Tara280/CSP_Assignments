
def inputs(type):
    return float(input(f"Monthly {type}"))

income = inputs("income: ")
rent = inputs("rent:")
utilities = inputs("utilities:")
groceries = inputs("groceries:")
transportation = inputs("transportation:")
savings = income*0.2
expenses = rent + utilities + groceries + transportation
spend = income-int(expenses)-savings

prent = rent/income*100
putilities = utilities/income *100
pgroceries = groceries/income *100
ptransportation = transportation/income *100
psavings = savings/income *100
pexpenses = expenses/income *100
print(f"Your rent is {int(prent)}% of your monthly income\n")
print(f"Your utilities is {int(putilities)}% of your monthly income\n")
print(f"Your groceries is {int(pgroceries)}% of your monthly income\n")
print(f"Your transportation is {int(ptransportation)}% of your monthly income\n")
print(f"Your savings is {int(psavings)}% of your monthly income\n")
print(f"Your expenses is {int(pexpenses)}% of your monthly income\n")