def run():
    # for count in range(1000):
    #     if count % 2 != 0:
    #         continue
    #     print(count)

    # for i in range(10000):
    #     print(i)
    #     if i == 5000:
    #         break

    name = input('Yor Name...: ')
    name = name.upper()
    for letter in name:
        print(letter)
        if letter == name[4]:
            break

if __name__ == '__main__':
    run()