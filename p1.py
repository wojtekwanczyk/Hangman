import sys, os, errno
from random import randint

words = []
filename = ""

# check if first argument is given (IndexError)
try:
    filename = sys.argv[1]
except IndexError as e:
    print("Give name of file as argument!\n" + str(e))
    exit(1)

# open file given in command line and convert to list
try:
    words = list(open(filename))
except FileNotFoundError as e:
    print("Error while opening the file!\n" + str(e))
    exit(1)


# take random word from the list
original_word = words[randint(0, len(words) - 1)]

# slice to remove the new line sign
original_word = original_word[:-1]

# working on list to replace letters on specific index
guessed_word = list("_" * len(original_word))
guessed_word_str = "".join(guessed_word)

print("Guess the word or I will hang you!\n"
      "Remember, you can make only 3 mistakes\n"
      "Your first letter?")

# cannot be more than 3
mistake_count = 0
used_letters = ""

while mistake_count < 4 and (original_word != guessed_word_str):

    # writing guessed word in proper format - print uses new line
    sys.stdout.write("\nWord: ")
    for c in guessed_word_str:
        sys.stdout.write(c + " ")
    print("")

    # get input
    letter = input().lower()

    # check if user gave only one sign
    if len(letter) > 1:
        mistake_count += 1
        print("You were supposed to write only one sign!\n"
              "It was your " + str(mistake_count) + " mistake!")
        continue

    # check if given sign is letter
    if not(letter.isalpha()):
        mistake_count += 1
        print("You were supposed to write a letter!\n"
              "It was your " + str(mistake_count) + " mistake!")
        continue

    # check if given letter was already typed
    if letter in used_letters:
        mistake_count += 1
        print("You have already typed this letter!\n"
              "It was your " + str(mistake_count) + " mistake!")
        continue
    else:
        used_letters += letter

    # check if given letter is in the word
    if letter in original_word:
        print("Yes! One step closer!")
        for i in range(len(original_word)):
            if letter == original_word[i]:
                guessed_word[i] = original_word[i]
    else:
        mistake_count += 1
        print("The word does not contain given letter!\n"
              "It was your " + str(mistake_count) + " mistake!")
        continue

    # make string to compare with  original_word
    guessed_word_str = "".join(guessed_word)


if mistake_count == 4:
    print("\nGAME OVER!\nThe word was:\n\n" + original_word.upper())
else:
    print("\n" + guessed_word_str.upper() +
          "\n\nCONGRATULATIONS! YOU HAVE WON!")
