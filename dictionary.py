def run():
    my_dictionary = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    # print(my_dictionary['llave1'])
    # print(my_dictionary['llave3'])
    # print(my_dictionary['llave2'])

    countries_population = {
        'Colombia': 50339443,
        'Argentina': 44938712,
        'Mexico': 127575529
    }

    # for country in countries_population.keys():
    #     print(country)

    # for country in countries_population.values():
    #     print(country)

    for country, population in countries_population.items():
        print(country + ' has ' + str(population) + ' inhabitants ')

if __name__ == '__main__':
    run()

# Colombia has 50339443 inhabitants
# Argentina has 44938712 inhabitants
# Mexico has 127575529 inhabitants