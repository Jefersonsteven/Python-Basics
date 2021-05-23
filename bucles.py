def run():
    LIMITED = 2000000
    count = 0
    powerTwo = 2**count
    while powerTwo < LIMITED:
        print('2 raised to ' + str(count) + ' equals ' + str(powerTwo))
        count += 1
        powerTwo = 2**count

if __name__ == '__main__':
    run()