def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    invertedWord = word[::-1]
    if word == invertedWord:
        return True
    else:
        return False


def run():
    word = input('Writing a word..❗❕.:')
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print('Is palindromo ✅')
    else:
        print('Not is palindromo ⛔')

if __name__ == '__main__':
    run()