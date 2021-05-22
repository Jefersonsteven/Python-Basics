currency = int(input("""
What is your coin 💵 ?
(1). 💲Pesos Colombians.
(2). 💲Pesos Argentines.
(3). 💲Pesos Mexicans.
:"""))

def currencyConverter(pesosNationDollar, nation):
    pesos = float(input('How much ' + nation + ' 💲pesos do you have?:'))
    dollars = pesos / pesosNationDollar
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print('you have 💲' + dollars + ' dollars')

if currency == 1:
    currencyConverter(3747.00, 'Colombians')
elif currency == 2:
    currencyConverter(94.29, 'Argentines')
elif currency == 3:
    currencyConverter(19.95, 'Mexicans')
else:
    print('we do not exchange bitcoins💲')