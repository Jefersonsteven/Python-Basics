def is_prime(number):
    count = 0
    for i in range(number):
        if number % ( i + 1 ) != 0:
            continue
        else:
            count +=1
    if count == 2:
        print('Is prime')
    else:
        print('Not is prime')

def run():
    number = int(input('Writing a number: '))
    is_prime(number)

if __name__ == '__main__':
    run()