"""
HANGMAN GAME - ASCII ART VERSION
Developed with Python 3.12
Features:
- Classic Hangman gameplay
- Randomized word selection
- Colorful console output
- Progress tracking
- Customizable difficulty
"""
import random
from time import sleep
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]

class HangmanGame:
    def __init__(self):
        self.word_bank = [
            "PYTHON", "JAVASCRIPT", "HANGMAN", "DEVELOPER", 
            "PROGRAMMING", "KEYBOARD", "MONITOR", "FUNCTION",
            "VARIABLE", "ALGORITHM", "SYNTAX", "DEBUGGING"
        ]
        self.max_attempts = 6
        self.reset_game()
        self.colors = {
            'title': '\033[1;36m',  # Cyan
            'correct': '\033[1;32m',  # Green
            'wrong': '\033[1;31m',  # Red
            'warning': '\033[1;33m',  # Yellow
            'highlight': '\033[1;35m',  # Purple
            'reset': '\033[0m'  # Reset color
        }

    def reset_game(self):
        self.secret_word = random.choice(self.word_bank)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.game_over = False
        self.display_word = ['_' for _ in self.secret_word]

    def display_title(self):
        title = r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
        """
        print(f"{self.colors['title']}{title}{self.colors['reset']}")
        print(f"{' ' * 20}by Python Wizard\n")

    def draw_hangman(self):
        print(HANGMAN_STAGES[self.incorrect_guesses])

    def show_word_progress(self):
        print("\nWord: ", end="")
        for letter in self.display_word:
            if letter in self.guessed_letters:
                print(f"{self.colors['correct']}{letter}{self.colors['reset']} ", end="")
            else:
                print("_ ", end="")
        print("\n")

    def show_guessed_letters(self):
        if self.guessed_letters:
            print("Guessed letters: ", end="")
            for letter in sorted(self.guessed_letters):
                if letter in self.secret_word:
                    print(f"{self.colors['correct']}{letter}{self.colors['reset']} ", end="")
                else:
                    print(f"{self.colors['wrong']}{letter}{self.colors['reset']} ", end="")
            print("\n")

    def get_player_input(self):
        while True:
            guess = input("Guess a letter: ").upper()
            if len(guess) != 1:
                print(f"{self.colors['warning']}Please enter a single letter.{self.colors['reset']}")
            elif not guess.isalpha():
                print(f"{self.colors['warning']}Please enter a valid letter (A-Z).{self.colors['reset']}")
            elif guess in self.guessed_letters:
                print(f"{self.colors['warning']}You've already guessed that letter!{self.colors['reset']}")
                self.show_guessed_letters()
            else:
                return guess

    def update_game_state(self, guess):
        self.guessed_letters.add(guess)
        if guess in self.secret_word:
            for i, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.display_word[i] = guess
            if '_' not in self.display_word:
                self.game_over = True
                print(f"\n{self.colors['correct']}Congratulations! You guessed the word: {self.secret_word}{self.colors['reset']}")
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_attempts:
                self.game_over = True
                self.draw_hangman()
                print(f"\n{self.colors['wrong']}Game Over! The word was: {self.secret_word}{self.colors['reset']}")

    def play_again(self):
        while True:
            choice = input("Would you like to play again? (Y/N): ").upper()
            if choice == 'Y':
                return True
            elif choice == 'N':
                return False
            else:
                print(f"{self.colors['warning']}Please enter 'Y' or 'N'.{self.colors['reset']}")

    def animate_intro(self):
        messages = [
            "Initializing Hangman...",
            "Selecting a secret word...",
            "Preparing the gallows...",
            "Ready to play!"
        ]
        for msg in messages:
            print(f"{self.colors['highlight']}{msg}{self.colors['reset']}")
            sleep(1)

    def play(self):
        self.display_title()
        self.animate_intro()
        
        while True:
            self.reset_game()
            
            while not self.game_over:
                print("\n" + "="*50)
                self.draw_hangman()
                self.show_word_progress()
                self.show_guessed_letters()
                
                guess = self.get_player_input()
                self.update_game_state(guess)

            if not self.play_again():
                print(f"\n{self.colors['title']}Thanks for playing! Goodbye!{self.colors['reset']}")
                break

if __name__ == "__main__":
    try:
        game = HangmanGame()
        game.play()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
