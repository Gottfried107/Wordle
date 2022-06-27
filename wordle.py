from words import word_list
from random import randint


# Ask the user to input a word and return it as a list made of its letters
def word_input():
    user_word = input('Enter a word: ')

    while len(user_word) != 5:
        user_word = input('The word must be five letters long. Try again: ')
    while user_word not in word_list:
        user_word = input('The word must be in word list. Try again: ')
    word_l = list(user_word)

    return word_l


# Check whether the user's word has any letters in common with the correct word
def word_check(user_word, correct_word):
    secret_word = list('-' * 5)
    used_letters = []

    # for each letter, get a list of all the occurences in user word and correct word
    for i in range(5):
        user_occ = []
        correct_occ = []

        letter = user_word[i]
        if letter in used_letters:
            continue
        used_letters.append(letter)

        n = 0
        for j in user_word:
            if j == letter:
                ind = user_word.index(j, n)
                user_occ.append(ind)
            n += 1

        n = 0
        for j in correct_word:
            if j == letter:
                ind = correct_word.index(j, n)
                correct_occ.append(ind)
            n += 1

        # check for correct positioins and substitute
        for j in user_occ:
            for k in correct_occ:
                if j == k:
                    secret_word[j] = letter.upper()
                    user_occ.remove(j)
                    correct_occ.remove(k)

        # check for wrong positions and substitute in the first occurrences of the word in the list
        for j in user_occ:
            for k in correct_occ:
                secret_word[j] = letter
                user_occ.remove(j)
                correct_occ.remove(k)

    return secret_word


# Check if the user has won
def win(user_word, correct_word):
    if user_word == correct_word:
        print(f'\nYou won! The word was {"".join(user_word)}.')
        return True

    return False


# Play the game asking the user's input 6 times
def play():
    for attempt in range(6):
        user_word = word_input()

        if win(user_word, correct_word) == True:
            return
        elif attempt < 5:
            print(''.join(word_check(user_word, correct_word)))
        else:
            print(f'Game over! The word was {"".join(correct_word)}.')


# Start playing!
if __name__ == '__main__':
    # choose word and create a list made of its letters
    correct_word = list(word_list[randint(0, len(word_list) - 1)])

    # instructions
    print('Wordle')
    print('A --> right letter, right place')
    print('a --> right letter, wrong place\n')

    # print the word using '-'
    print('-'*5)

    play()