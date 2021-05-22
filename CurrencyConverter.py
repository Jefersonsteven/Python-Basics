currency = int(input("""
What is your coin 💵 ?
(1). 💲Pesos Colombians.
(2). 💲Pesos Argentines.
(3). 💲Pesos Mexicans.
:"""))
Pesos_Colombians_In_Dollar = 3747.00
Pesos_Argentines_In_Dollar = 94.29
Pesos_Mexicans_In_Dollar = 19.95

if currency == 1:
    pesos = float(input('How much Colombian 💲pesos do you have?:'))
    dollars = pesos / Pesos_Colombians_In_Dollar
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print('you have 💲' + dollars + ' dollars')
elif currency == 2:
    pesos = float(input('How much Argentines 💲pesos do you have?:'))
    dollars = pesos / Pesos_Argentines_In_Dollar
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print('you have 💲' + dollars + ' dollars')
elif currency == 3:
    pesos = float(input('How much Mexicans 💲pesos do you have?:'))
    dollars = pesos / Pesos_Mexicans_In_Dollar
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print('you have 💲' + dollars + ' dollars')
else:
    print('we do not exchange bitcoins💲')