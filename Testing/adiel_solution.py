secret_word = list("table")
old_guessed_letter = [ ]
hidden_word = [ ]
guess = input("guess a letter: ")

old_guessed_letter.append(guess)

index = 0  # Where we are in the index

for index_letter in secret_word:
    index = secret_word.index(index_letter)
    # print("index letter from the loop:", index_letter)
    # print("secret word:", secret_word)
    # print("index:", index)


def show_hidden():
    pass