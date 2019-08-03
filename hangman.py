import random

word_list = ["hello", "world", "newspaper", "muffin", "apple", "mango", "pear", "tea", "coffee", "mug", "chair", "table", "water"]

def start_game ():
    print("Welcome to Hangman! We hope you're ready to enjoy a tough game")
    word = word_list[random.randint(0,len(word_list))]
    return word


def enter_letter():
    letter = ""
    while len(letter) != 1:
        user_input = input("Please enter a letter: ")
        if type(user_input) == str and len(user_input) == 1:  #userinput is always a string
            letter = user_input
            return letter
        else:
            print ("Please follow the directions")

def track_word_progress(word,letter):
    if letter in word:


def gameplay():
    word = start_game()
    word_length = len(word)
    solved = False
    print("The word you are solving for has {0} letters".format(word_length))
    print("_ " * word_length)
    while solved == False:
        letter = enter_letter()
        track_word_progress(word,letter)



gameplay()