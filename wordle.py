"""
Wordle: A game where the User Guesses the Random Word.
"""

from colorama import Fore, Back, Style   # Imports 'colorama' library that adds style features to output in the terminal.
import random                            # Imports 'random' library that generates a random int.

# Styling Elements
green_h = Back.GREEN      # Highlights Green
yellow_h = Back.YELLOW    # Highlights Yellow
red_h = Back.RED          # Highlights Red
yellow_l = Fore.YELLOW    # Yellow Letter
red_l = Fore.RED          # Red Letter
bold = Style.BRIGHT       # Bold Letter
reset = Style.RESET_ALL   # Reset Styling Elements

# List of four letter words
four_letter_words = [
    'area', 'army', 'baby', 'back', 'ball', 'band', 'bank', 'base', 'bite', 'blue', 'body', 'book', 'cake', 'call', 'card',
    'care', 'case', 'cash', 'cave', 'city', 'club', 'cost', 'date', 'deal', 'disk', 'door', 'east', 'face', 'fact', 'fwesarm',
    'fear', 'film', 'fire', 'fish', 'food', 'foot', 'foul', 'game', 'girl', 'glow', 'goal', 'gold', 'hair', 'half', 'hall',
    'hand', 'head', 'help', 'hike', 'hill', 'home', 'hope', 'hour', 'hype', 'icon', 'idea', 'iron', 'jazz', 'kind', 'king',
    'kite', 'lady', 'land', 'lazy', 'life', 'lime', 'line', 'list', 'look', 'lord', 'loss', 'love', 'mind', 'miss', 'move',
    'mute', 'name', 'need', 'nerd', 'news', 'note', 'page', 'pain', 'pair', 'park', 'part', 'past', 'path', 'plan', 'play',
    'post', 'quit', 'quiz', 'race', 'rain', 'rate', 'rest', 'ride', 'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule',
    'sale', 'seat', 'shop', 'show', 'side', 'sign', 'size', 'skin', 'song', 'sort', 'star', 'step', 'task', 'team', 'test',
    'text', 'time', 'toss', 'tour', 'town', 'tree', 'turn', 'type', 'ugly', 'user', 'vibe', 'view', 'wall', 'wavy', 'weak',
    'week', 'west', 'wife', 'wild', 'will', 'wind', 'wine', 'wood', 'word', 'work', 'yarn', 'yawn', 'year', 'zero', 'zone']

# List of five letter words
five_letter_words = [
    'about', 'actor', 'adult', 'agree', 'alarm', 'alive', 'angel', 'angry', 'apple', 'award', 'basic', 'beach', 'beach', 
    'bench', 'black', 'blaze', 'blind', 'blood', 'brain', 'bread', 'brown', 'cable', 'chain', 'chair', 'cheap', 'child', 
    'china', 'class', 'clean', 'clear', 'clock', 'crime', 'dance', 'death', 'dream', 'dress', 'drill', 'drink', 'drive', 
    'early', 'earth', 'enjoy', 'extra', 'faith', 'false', 'field', 'fifth', 'fifty', 'fight', 'final', 'first', 'floor', 
    'force', 'forth', 'forty', 'fruit', 'funny', 'glass', 'globe', 'grade', 'grass', 'green', 'hands', 'happy', 'heart',
    'horse', 'horse', 'house', 'human', 'image', 'juice', 'large', 'laugh', 'learn', 'lucky', 'magic', 'march', 'money',
    'month', 'motor', 'mouse', 'mouth', 'movie', 'music', 'night', 'north', 'nurse', 'ocean', 'paint', 'paper', 'party',
    'peace', 'phone', 'photo', 'pizza', 'plane', 'plant', 'power', 'price', 'print', 'prize', 'queen', 'radio', 'right',
    'river', 'score', 'seven', 'shape', 'share', 'shoot', 'short', 'sleep', 'small', 'smart', 'smile', 'sorry', 'sound',
    'south', 'space', 'speed', 'sport', 'staff', 'stone', 'store', 'sugar', 'table', 'teeth', 'texas', 'thank', 'theft',
    'theme', 'three', 'today', 'train', 'truck', 'trust', 'uncle', 'under', 'valid', 'video', 'voice', 'watch', 'water',
    'wheel', 'white', 'woman', 'world', 'wrong', 'young', 'zebra']

# List of six letter words
six_letter_words = [
    'acting', 'action', 'active', 'addict', 'advice', 'afford', 'afraid', 'animal', 'answer', 'artist', 'assist', 'attack',
    'august', 'author', 'banana', 'basket', 'battle', 'beaker', 'beauty', 'became', 'beetle', 'before', 'behind', 'belong',
    'better', 'bishop', 'bottom', 'branch', 'breath', 'bridge', 'bright', 'budget', 'button', 'cactus', 'camera', 'cancer',
    'candle', 'canyon', 'carbon', 'career', 'casino', 'castle', 'casual', 'caught', 'cereal', 'chance', 'change', 'charge',
    'cheese', 'cherry', 'driver', 'choice', 'church', 'cinema', 'circle', 'coffee', 'combat', 'common', 'copper', 'corner',
    'county', 'couple', 'course', 'cousin', 'create', 'crisis', 'damage', 'danger', 'dealer', 'debate', 'decade', 'defeat',
    'defend', 'degree', 'demand', 'desert', 'design', 'detail', 'device', 'dinner', 'direct', 'doctor', 'dollar', 'donate',
    'double', 'dragon', 'eating', 'editor', 'effort', 'eleven', 'engine', 'fabric', 'family', 'female', 'forest', 'french',
    'fridge', 'friend', 'future', 'gadget', 'garage', 'gender', 'genius', 'german', 'google', 'grapes', 'hammer', 'hustle',
    'insect', 'jigsaw', 'lagoon', 'leader', 'liquid', 'memory', 'nugget', 'online', 'outfit', 'paddle', 'peanut', 'pencil',
    'people', 'pepper', 'pretty', 'repeat', 'reward', 'rhythm', 'school', 'screen', 'search', 'season', 'senior', 'shadow',
    'shower', 'shrimp', 'silver', 'smooth', 'soccer', 'spider', 'spirit', 'street', 'stress', 'studio', 'tattoo', 'ticket',
    'window', 'winner', 'wisdom', 'wizard', 'yellow', 'yogurt']

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
Generates a random word from list based on length of word.
Uses 'level' parameter from user to determine which list to use.
Returns a random word.
"""
def generate_rand_word(level):
    num = random.randint(0,150)
    if level == 4:
        return list(four_letter_words[num])
    elif level == 5:
        return list(five_letter_words[num])
    else:
        return list(six_letter_words[num])

"""
Outputs Game Instructions to the user.
Uses 'level' parameter to output random word length and number of attempts.
"""
def game_instructions(level):
    print(f"You have {bold}{yellow_l}{level}{reset} tries to guess the {bold}{yellow_l}{level}{reset}-letter word I'm thinking of")
    print(f"{green_h}{bold}Green{reset} = Letter in Exact Position")
    print(f"{yellow_h}{bold}Yellow{reset} = Letter is in word but in Different Position")
    print(f"{red_h}{bold}Red{reset} = Letter is not in word")


"""
Prompts User to attempt to guess the word and checks if word inputted is correctly formatted.
Uses 'level' paramter to check attempted word length.
Uses 'num' paramter to display Attempt number.
Returns User's Attempted word.
"""
def get_user_guess(level, num):
    while True:
        guess = input(f"Attempt {yellow_l}{bold}{num + 1}{reset}: ").lower()
        if len(guess) == level and not any(char.isdigit() for char in guess):
            return guess
        elif any(char.isdigit() for char in guess):
            print("Error. Inputted attempt must only include letters.")
        else:
            print(f"Error. Inputted word must be a {level}-letter word!")

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
    attempt = 0
    # Will run until max number of attempts set by level or random word is guessed by user.
    while attempt < level:
        # Prompt user to guess the random word and covert to list.
        user_guess = list(get_user_guess(level, attempt))
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
            # Print out letters with their colors.
            for i in range(level):
                print(f"{color[i]}{bold}{user_guess[i]}{reset}", end = "")
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
        print("Word Guessed Correctly! You win.")
    else:
        print(f"Word was {red_l}{bold}not{reset} Guessed. Word = {yellow_l}{bold}{''.join(random_word)}{reset}")
        print("Better luck next time.")

# Main Function of the Program
def main():
    print(f"{red_h}{bold}Welcome to Worlde!{reset}")
    mode = user_dif_mode()
    random_word = generate_rand_word(mode)
    game_instructions(mode)
    word_guessed = game(mode, random_word)
    check_win(word_guessed, random_word)

if __name__ == "__main__":
    main()
