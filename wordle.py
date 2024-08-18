"""
Wordle: A game where the User Guesses the Random Word.
"""

from colorama import Fore, Back, Style   # Imports 'colorama' library that adds style features to output in the terminal.
import openai                            # Imports 'openai' library to use ChatGPT to generate random word.


# Openai API Key



# Styling Elements
green_h = Back.GREEN      # Highlights Green
yellow_h = Back.YELLOW    # Highlights Yellow
red_h = Back.RED          # Highlights Red
yellow_l = Fore.YELLOW    # Yellow Letter
red_l = Fore.RED          # Red Letter
bold = Style.BRIGHT       # Bold Letter
reset = Style.RESET_ALL   # Reset Styling Elements


"""
Prompts User for Difficulty Mode. Checks if only a word is inputted.
Returns a int that represents the length of the random word.
"""
def user_dif_mode():
    while True:
        dif = input(f"Type In a Difficulty Mode ({green_h}{bold}Easy{reset}, {yellow_h}{bold}Hard{reset}, {red_h}{bold}Challenge{reset}): ").lower()
        if dif == "easy":
            return 4
        elif dif == "hard":
            return 5
        elif dif == "challenge":
            return 6
        else:
            print("Error. Please try again")


"""
Openai Function that sends response to ChatGPT and returns it's response.
"""
def open_ai(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content.strip()


"""
Generates a random word using the ChatGPT API.
Returns a random word.
"""
def generate_rand_word(level):
    return list(open_ai(f"Give me a common word with a length of {level} that can be easily guessed for a Wordle game. Only return just the lowercased word and nothing else."))
    

"""
Outputs Game Instructions to the user.
Uses 'level' parameter to output random word length and number of attempts.
"""
def game_instructions(level):
    print(f"\nYou have {bold}{yellow_l}{level}{reset} tries to guess the {bold}{yellow_l}{level}{reset}-letter word I'm thinking of")
    print(f"{green_h}{bold}Green{reset} = Letter in Exact Position")
    print(f"{yellow_h}{bold}Yellow{reset} = Letter is in word but in Different Position")
    print(f"{red_h}{bold}Red{reset} = Letter is not in word\n")
    print(f"{yellow_l}{bold}Stuck?{reset} Needing a {yellow_l}{bold}hint?{reset} Just type {yellow_l}{bold}y{reset} to use up to {yellow_l}{bold}{level - 2}{reset}\n")


"""
Generates a hint to help the user guess the word.
Uses 'level' parameter from user to determine which list to use.
Returns a random word.
"""
def generate_Hint(guess):
    return open_ai(f"Give the user a hint to guess the word {guess}")


"""
Prompts User to attempt to guess the word and checks if word inputted is correctly formatted.
Uses 'level' paramter to check attempted word length.
Uses 'num' paramter to display Attempt number.
Returns User's Attempted word.
"""
def get_user_guess(level, r_word, attempt, hint):
    while True:
        guess = input(f"Attempt {yellow_l}{bold}{attempt + 1}{reset}: ").lower()
        if len(guess) == level and not any(char.isdigit() for char in guess):
            return guess
        elif guess == "y":
            if hint == level - 2:
                print("You are all out of hints!\n")
            else:
                print(f"Hint {yellow_l}{bold}{hint+1}{reset}: {generate_Hint(r_word)}\n")
                hint += 1
        elif any(char.isdigit() for char in guess):
            print("Error. Inputted attempt must only include letters.\n")
        else:
            print(f"Error. Inputted word must be a {level}-letter word!\n")
   

"""
Compares user's guess to the random word.
Uses 'level' parameter to set number of attempts.
'r_word' parameter is the random word generated.
If attempted word equals the random word then it highlights each letter Green and returns True.
Otherwise, it iterates through the attempted guess, and highlights each letter based on the random word.
    If letter is in exact position as random word, highlight letter Green.
    If letter is not in the same position as random word but is in word, highlight Yellow.
    If letter is not in random word (or no more of the same letter in word), highlight letter Red.
After all attempts, If word is not guessed return False.
"""
def game(level, r_word):
    # Variables to hold number of attempts and hints used
    attempt = 0
    hint = 0
    guesses_colors = []
    guesses = []

    # Will run until max number of attempts set by level or random word is guessed by user.
    while attempt < level:
        # Prompt user to guess the random word and covert to list.
        user_guess = list(get_user_guess(level, r_word, attempt, hint))

        # If user guesses the random word, break the loop and return True.
        if user_guess == r_word:
            print(f"{green_h}{bold}{''.join(r_word)}{reset}")
            return True
        
        # Else, iterate and compare user's guess word to random word.
        else:
            # Compare a letter at a time.
            # Make a list that holds the color values for each letter in guessed.
            color = [None] * level

            # Make a list that holds the available letters. This prevents repeated letters
            # turning yellow.
            available_letters = r_word[:]

            # Iterate through every letter first to macth green letters and remove from availabe
            # letters.

            for i in range(level):
                # If current letter in user guess matches random word in same position,
                # input green in list color in the same index and remove from avaiilable letters.
                if user_guess[i] == r_word[i]:
                    color[i] = green_h
                    available_letters.remove(user_guess[i])

            # Iterate again but for yellow and red letters.
            for i in range(level):
                # This if will prevent already green letters to be modifed.
                if color[i] == None:
                    # Iterate through available_letters. If letter in user guess matches any,
                    # remove the letter from available letters and make the color yellow.
                    for j in range(len(available_letters)):
                        if user_guess[i] == available_letters[j]:
                            color[i] = yellow_h
                            available_letters.remove(user_guess[i])
                            break
                        # If no matches, then make color red.
                        else:
                            color[i] = red_h

            guesses_colors.append(color)
            guesses.append(user_guess)

            # Print out letters with their colors.
            for i in range(len(guesses_colors)):
                print(f"{yellow_l}{bold}{i+1}.{reset} ", end="")
                for j in range(len(guesses_colors[i])):
                    print(f"{guesses_colors[i][j]}{bold}{guesses[i][j]}{reset}", end = "")
                print("")
            print("")
        print("")

        attempt += 1
    return False


"""
Checks for winner and loser and prints Result.
'word_guess' parameter is a boolean that tells function if winner or loser.
    If True, it prints word is guess correctly.
    Else False, it prints word is not guess correctly and prints 'r_word' parameter which is the random word.
"""
def check_win(word_guessed, random_word):
    if word_guessed:
        print("Word Guessed Correctly! You win!\n")
    else:
        print(f"Word was {red_l}{bold}not{reset} Guessed. Word = {yellow_l}{bold}{''.join(random_word)}{reset}")
        print("Better luck next time.\n")



# Main Function of the Program
def main():
    print(f"\n{red_h}{bold}Welcome to Worlde!{reset}")
    mode = user_dif_mode()
    random_word = generate_rand_word(mode)
    game_instructions(mode)
    word_guessed = game(mode, random_word)
    check_win(word_guessed, random_word)

if __name__ == "__main__":
    main()
