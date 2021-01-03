import os
import random

def random_word_generator(dic):
    seed = int(random.random()*len(dic))
    return dic[seed]

def right_guessed_word(secret_word, guessed_word):
    for i in range(len(guessed_word)):
        if secret_word[i] != guessed_word[i]:
            return False
    return True

def show(word):
    for char in word:
        print(char, end=" ")
    print("\n")

try:
    dirname = os.path.dirname(__file__)
    f = open(dirname + "/words.txt",mode="r")
    dic = f.read().split('\n')
except FileNotFoundError:
    f = open(dirname + "./words.txt",mode="r")
    dic = f.read().split('\n')


secret_word = random_word_generator(dic)
wrong_guesses = 0
guessed_word = ["_" for i in range(len(secret_word))]
guesses = []

while wrong_guesses < 6 and not right_guessed_word(secret_word, guessed_word):
    show(guessed_word)
    guess = input("Guess a letter or a word: ")
    if guesses.__contains__(guess):
        print("You already guessed this, try again.")
        continue
    guesses.append(guess)
    if len(guess) == 1:
        guessed_right = False
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                guessed_word[i] = guess
                guessed_right = True
        if guessed_right == True:
            print("Right! You are one step closer to victory!")
            continue

    if guess == secret_word:
        guessed_word = guess
        break 
    else:
        guessed_right = False
    
    if not guessed_right:
        wrong_guesses += 1
        print("You guessed wrong, Too bad! " + str(6 - wrong_guesses) + " guesses remaining")
        continue

    print("Invalid response.")




if right_guessed_word(secret_word, guessed_word):
    print("You won! Congratulations!")

else: 
    print("Too bad! The secret word was " + secret_word)
