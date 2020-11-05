import random


def play():
    print('H A N G M A N')
    tiny_list = ['python', 'java', 'kotlin', 'javascript']
    random.shuffle(tiny_list)
    word = tiny_list[0]
    life = 8
    word_completion = '-' * len(word)
    guessed_letters = []
    guessed_words = []
    lower = ('abcdefghijklmnopqrstuvwxyz')
    while life > 0:
        print('')
        print('{}'.format(word_completion))
        guess = input('Input a letter: ')
        if len(guess) == 1 and guess in lower:
            if guess in guessed_letters:
                print("You've already guessed this letter")
            elif guess not in word:
                print("That letter doesn't appear in the word")
                life -= 1
                guessed_letters.append(guess)
            else:
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
        else:
            if len(guess) > 1:
                print("You should input a single letter")
            elif guess == '' and ' ':
                print("You should input a single letter")
            else:
                print("Please enter a lowercase English letter")
    if life > 0:
        print('')
        print('You guessed the word {}!'.format(word))
        print('You survived!')
    else:
        print('You lost!')



while True:
    print('Type "play" to play the game, "exit" to quit:')
    answer = input()
    if answer == 'play':
        play()
    elif answer == 'exit':
        exit()