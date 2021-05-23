import random

def run():
    random_number = random.randint(1, 100)
    chosen_number = int(input('choose a number from 0 to 100: '))
    while chosen_number != random_number:
        if chosen_number < random_number:
            print('The number is greater')
        else:
            print('The number is less')
        chosen_number = int(input('choose a number from 0 to 100: '))
    print('WINNER!')

if __name__ == '__main__':
    run()