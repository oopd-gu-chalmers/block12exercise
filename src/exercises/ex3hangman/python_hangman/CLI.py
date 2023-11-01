# package exercises.ex4hangman

import os.path
from HangMan import Result, HangMan
from FileService import FileService

# Command Line Interface for Hangman OO model
# No game logic allowed here, only player interaction
#
# Run this to run the game
#
# See
# - usemoreclasses/
# - UseExceptions
from Secret import Secret
from Man import Man

DEFAULT_PATH = os.path.join("words.txt")


def play_hangman_cli():
    game, man, secret, the_word = setup_game()
    welcome_msg(len(the_word))
    run_game_loop(game, man, secret)
    win_msg(game.get_result(), game.get_nr_of_guesses(), the_word)


def setup_game():
    the_word = fetch_random_word()
    secret = Secret(the_word)
    man = Man()
    game = HangMan(man, secret)
    return game, man, secret, the_word


def run_game_loop(game, man, secret):
    while not game.is_over():
        char_guessed = guess_character()
        was_correct = game.update(char_guessed)
        print_status(char_guessed, was_correct, secret, man)


def fetch_random_word():
    the_word = ""
    try:
        the_word = FileService.get_random_word_from_file(DEFAULT_PATH)
    except IOError as ioe:
        plot_exception(ioe)
        exit(0)
    return the_word


def print_status(ch, was_correct_guess, secret, man):
    correct_str = "correct" if was_correct_guess else "incorrect"
    print(f"Your guess {ch} was {correct_str}. Current status:")
    print()
    print(f"The word: {secret}")
    print()
    print(man)


def guess_character():
    while True:
        character = input("Enter a character > ")
        if len(character) == 1 and character.isalpha():
            break
    return character


def welcome_msg(word_length):
    print("Welcome to HangMan, try to guess the word! It's " +
          str(word_length) + " characters long")


def win_msg(result, nr_guesses, answer):
    if result == Result.WIN:
        print(f"You made it. You needed {nr_guesses} tries.")
    else:
        print("Sorry you lost. Word(s) was: " + answer)


def plot_exception(e):
    print("Exception: " + str(e))


if __name__ == "__main__":
    play_hangman_cli()

# def plot_mask(mask):
#     for ch in mask:
#         print(ch + " ")
#     print()
#
#
# def plot_man(health: int):
#     for part in parts:
#         print(part, end='')
#     if health in [1, 3, 4]:  # Layout
#         print()


