pesos = input('How much Colombian pesos do you have?: ')
pesos = float(pesos)
value_dollar = 3721.57
dollars = pesos / value_dollar
dollars = round(dollars, 2)
dollars = str(dollars)
print('you have $' + dollars + ' dollars')