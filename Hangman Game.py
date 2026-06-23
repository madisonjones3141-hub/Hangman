# Hangman Game

import random
solution = 0 # placeholder for the true word. The solution is the actual word the user is trying to guess.
hidden_word = 0 # placeholder for resetting the new word. The hidden word is what the computer displays to allow the user to guess.
number_of_guesses = 0 # how many times they've guessed
guess = 13 # how many guesses remain
letters_guessed = set() # letters they've guessed
score = 10000
hint = random.randint(0, 4)
index = random.randint(0, 9)
word_conversion = {4: 0, 5: 1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6, 11: 7, 12: 8} # converting word_length variable into an index
mary_poppins = False
wordbank = (
    ('JAWS', 'STAR', 'BITE', 'JERK', 'FOXY', 'CATS', 'BUCK', 'WAXY', 'MAZE', 'STAY'),
    ('JAZZY', 'DOZEN', 'BANJO', 'WATER', 'WHITE', 'PARTY', 'SCARF', 'COMIC', 'CHUCK', 'BLADE'),
    ('COFFEE', 'ABROAD', 'CORNER', 'BELONG', 'DEMAND', 'CIRCLE', 'COLUMN', 'DEPUTY', 'DESERT', 'ANIMAL'),
    ('ABANDON', 'CABBAGE', 'EYEDROP', 'HABITAT', 'ICEBERG', 'OARFISH', 'SABBATH', 'UKULELE', 'VACANCY', 'TADPOLE'),
    ('ABSOLUTE', 'CELLULAR', 'CROSSING', 'DELIVERY', 'COLORFUL', 'FOOTBALL', 'HISTORIC', 'INTERNAL', 'LAUGHTER', 'PAINTING'),
    ('AFTERNOON', 'BOYFRIEND', 'DISCOVERY', 'COMMUNITY', 'DIFFERENT', 'IMPORTANT', 'HYDRATION', 'EAGERNESS', 'SABOTAGED', 'WALLPAPER'),
    ('ANABAPTIST', 'DAFFODILS', 'EARTHBOUND', 'FABRICATOR', 'IRONICALLY', 'OBLIGATORY', 'PEACEMAKER', 'RABBITHOLE', 'TABERNACLE', 'UBIQUITOUS'),
    ('EARTHENWARE', 'NAILCLIPPER', 'TABLESPOONS', 'VACATIONING', 'RACQUETBALL', 'RAINFORESTS', 'PADDLEBOARD', 'PANDEMONIUM', 'OBLITERATED', 'MICROSCOPIC'),
    ('ABBREVIATION', 'BACHELORETTE', 'EARSPLITTING', 'HABILITATION', 'KALEIDOSCOPE', 'NAMELESSNESS', 'RACKETEERING', 'WAINSCOTTING', 'TECHNICALITY', 'ACCIDENTALLY')
)
hangedman_line1 = [".         .", ".         .", "|         .", ".         .", "________   ", "________", "________", "________", "________", "________", "________", "________", "________", "________"]
hangedman_line2 = ["           ", "           ", "|          ", "|          ", "|          ", "|/      ", "|/   |  ", "|/   |  ", "|/   |  ", "|/   |  ", "|/   |  ", "|/   |  ", "|/   |  ", "|/   |  "]
hangedman_line3 = ["           ", "           ", "|          ", "|          ", "|          ", "|       ", "|       ", "|    O  ", "|    O  ", "|    O  ", "|    O       ", "|    O       ", "|    O       ", "|    X   GAME"]
hangedman_line4 = ["           ", "           ", "|          ", "|          ", "|          ", "|       ", "|       ", "|       ", "|    |  ", "|   /|  ", "|   /|\\ ", "|   /|\\ ", "|   /|\\ ", "|   /|\\  OVER"]
hangedman_line5 = ["           ", "           ", "|          ", "|          ", "|          ", "|         ", "|         ", "|        ", "|         ", "|        ", "|         ", "|   /", "|   / \\ ", "|   / \\ "]
hangedman_line6 = [".         .", "___________", "|__________", "|\\_________", "|\\________", "|\\_________", "|\\_________", "|\\_________", "|\\_________", "|\\_________", "|\\_________", "|\\_________", "|\\_________"]


word_length = "A!@#$%^&*="      # Validating word length
while not str(word_length).isnumeric() or not (3 < int(word_length) < 12):
    if word_length == "A!@#$%^&*=":
        word_length = input("Welcome to HANGMAN! How long should the word be? \n4 to 12 letters, please: ")
    try:
        word_length = int(word_length)
        if word_length == 0:
            word_length = (random.randint(4, 12))
            print("Unl0ck3D 5uP3r ult1mat3 R4ND0m m0d3! Now generating random word...\nRandom word generated.")
        elif word_length == 64:
            mary_poppins = True
            solution = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS"
            word_length = int(len(solution))
            break
        elif word_length < 4:
            word_length = input("You know, shorter words are actually harder... \nListen, I just need you to pick a number greater than 4 so I can pick a word for you: ")
        elif word_length > 12:
            word_length = input("Is \'Supercalifragilisticexpialidocious\' okay with you? \nJust pick a number less than 12 so I can get a good word for you: ")
    except:
        word_length = input("I... I don't know what to make of that. Look, just pick a number between 4 and 12: ")

print(f"Okay... Lemme think, here. A word with {word_length} letters... Got it!")

# Establishing word length
if mary_poppins == False:
    solution = wordbank[word_conversion[word_length]][index]
hidden_word = len(solution) * '_'

print(f"The word is: ", hidden_word)
print(hangedman_line1[number_of_guesses])
print(hangedman_line2[number_of_guesses])
print(hangedman_line3[number_of_guesses])
print(hangedman_line4[number_of_guesses])
print(hangedman_line5[number_of_guesses])
print(hangedman_line6[number_of_guesses])
while number_of_guesses < 13:
    user_guess = input(f"You have {guess} guesses remaining. Type \'?\' to view a hint or \'!\' to view your past guesses. Choose a single letter to guess: ").upper()
    while not user_guess.isalpha() or not len(user_guess) == 1 or user_guess in letters_guessed:        # Validating user-input guess
        if user_guess == "404":
            user_guess = input(f"The word is {solution}. Press a key to continue. ").upper()     # revealing the answer for debugging
            continue
        if user_guess == "?":
            user_guess = input("Are you sure you want to use a hint? This will cost 2 guesses. Type \"?\" again to confirm, or a letter to guess normally: ").upper()   # giving a hint
            if user_guess == "?":
                while solution[hint] in letters_guessed:
                    hint = random.randint(0, int(word_length))
                user_guess = input(f"It may behoove you to try {solution[hint]} ;) ").upper()
                guess -= 2
                score -= 1246
            continue
        if user_guess == "!":
            if len(letters_guessed) > 0:
                user_guess = input(f"You've guessed {letters_guessed}. You have {guess} guesses remaining. Type \'?\' to view a hint or choose a single letter to guess:  ").upper()
            else:
                user_guess = input(f"Short-term memory loss, eh? It's fine! Happens  to everyone! You haven't guessed anything yet, so go ahead and guess a letter: ").upper()
            continue
        if len(user_guess) > 1:
            user_guess = input("Well, you can only guess one letter at a time. Try again: ").upper()
            continue
        elif user_guess in letters_guessed:
            user_guess = input("Oops! You already guessed that one. Try again: ").upper()
            continue
        else:
            user_guess = input("That entry was invalid. Try entering a capital letter, like \"N\": ").upper()
            continue
    letters_guessed.add(user_guess)
    num_occurrences = solution.count(user_guess)
    position = -1
    for occurrence in range(num_occurrences):          # Finding/placing user input guess in the hidden word
        position = solution.find(user_guess, position+1)
        hidden_word = hidden_word[:position] + user_guess + hidden_word[position+1:]
    if user_guess in hidden_word:
        print("Correct! The word is now: ", hidden_word)
    else:
        print(f"Uh oh! That one wasn't in there. The word is still: {hidden_word}")
        guess -= 1
        score -= 623
        number_of_guesses += 1
        print(hangedman_line1[number_of_guesses])
        print(hangedman_line2[number_of_guesses])
        print(hangedman_line3[number_of_guesses])
        print(hangedman_line4[number_of_guesses])
        print(hangedman_line5[number_of_guesses])
        print(hangedman_line6[number_of_guesses])
    if not '_' in hidden_word:
        break

if '_' not in hidden_word:
    print(f"You won with a score of {score}!! The word was {solution}")
else:
    print(f"Better luck next time! The word was {solution}")

