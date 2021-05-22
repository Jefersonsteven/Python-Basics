dollar= input('How much dollars do you have?: ')
dollar = float(dollar)
value_dollar_in_colombian = 3721
pesos_colombian = value_dollar_in_colombian * dollar
pesos_colombian = int(pesos_colombian)
pesos_colombian = str(pesos_colombian)
print('you have $' + pesos_colombian + ' pesos Colombian')