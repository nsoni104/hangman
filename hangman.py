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

def letter_in_word(word,letter):
    if letter in word:
        return True
    else:
        return False


def track_word(word,letter):
    list_word = list(word)
    print(list_word)
    letter_index = []
    for i, _ in enumerate(list_word):
        print(i)
        if list_word[i] == letter:
            print(list_word[i])
            num = i
            letter_index.append(num)
            #print("{0} was found!".format(letter))
    for i in letter_index:
        list_word[i] = letter
    print("Your chosen letter {0} was found {1} times in the word".format(letter,len(letter_index)))
    print(letter_index)



def gameplay():
    word = start_game()
    word_length = len(word)
    letters_guessed = []
    guesses = 0
    solved = False
    print("The word you are solving for has {0} letters".format(word_length))
    user_word = "_ " * word_length
    print(user_word)
    while solved == False:
        letter = enter_letter()
        if letter_in_word(word,letter) and letter not in letters_guessed:
            print("Correct!")
            track_word(word,letter)
        else:
            guesses += 1
            print("Sorry, the word doesn't contain {0}.".format(letter))
            print("You've now had {0} guesses.".format(guesses))


print(track_word("applep","p"))