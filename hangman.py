import random

word_list = ["hello", "world", "newspaper", "muffin", "apple", "mango", "pear", "tea", "coffee", "mug", "chair", "table", "water"]

def start_game ():
    print("Welcome to Hangman! We hope you're ready to enjoy a tough game")
    difficulty = input("How hard of a game do you want to have? You can enter (e)asy,(m)edium,or (h)ard: ")
    word = word_list[random.randint(0,len(word_list))]
    if difficulty == "e":
        max_guess = 25
    elif difficulty == "m":
        max_guess = 17
    else:
        max_guess = 10
    print("You have a maximum of {0} guesses before the hangman hangs your man".format(max_guess))
    return word,max_guess

def list_to_string(user_list):
    new_string = ""
    for i in user_list:
        new_string += i
    return new_string


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


def track_word(word,user_word,letter):
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
        user_word[i] = letter
    if len (letter_index) == 1:
        print("Your chosen letter {0} was found 1 time in the word".format(letter))
    else:
        print("Your chosen letter {0} was found {1} times in the word".format(letter,len(letter_index)))
    return user_word



def gameplay():
    word,max_guess = start_game()
    word_length = len(word)
    letters_guessed = []
    guesses = 0
    solved = False
    print("The word you are solving for has {0} letters".format(word_length))
    user_word = ["_" for i in range(0,word_length)]
    while solved == False:
        if guesses > max_guess:
            print("Sorry you lose! The hangman hung your man.")
            return
        letter = enter_letter()
        if letter_in_word(word,letter) and letter not in letters_guessed:
            guesses += 1
            print("Correct!")
            track_word(word, user_word, letter)
            print(list_to_string(user_word))
            print("You've now had {0} guesses.".format(guesses))
            if list_to_string(user_word) == word:
                solved = True
        else:
            guesses += 1
            letters_guessed.append(letter)
            print("Sorry, the word doesn't contain {0}.".format(letter))
            print("You've now had {0} guesses.".format(guesses))
    print ("Congratulations! You win Hangman! It took you {0} guesses.".format(guesses))
    return


#print(track_word("applep",["_","_","_","_","_","_"],"p"))
gameplay()
#print(list_to_string(["h","e","llo"]))