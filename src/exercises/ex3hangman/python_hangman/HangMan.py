# package exercises.ex4hangman

#  The Hangman game (in a text version)
#  This is the game logic
#
#  This illustrated the concept of an "OO-model" (i.e. many connected
#  objects from different classes). Objects working together to solve a problem.
from enum import Enum, auto

from Secret import Secret  # From the *file* Secret, import the *class name* Secret
from Man import Man


class Result(Enum):
    NONE = auto()
    WIN = auto()
    LOSE = auto()


class HangMan:
    def __init__(self, man: Man, secret: Secret):
        self.__man = man        # Other object in model
        self.__secret = secret  # Other object in model
        self.__nr_guesses = 0
        self.__result = Result.NONE

    # The game logic
    def update(self, ch: str) -> bool:
        was_correct = self.__handle_guess(ch)
        if not was_correct:
            self.__man.increment_hanging()
            if self.__man.is_hung():
                self.__result = Result.LOSE
        else:
            if self.__secret.is_fully_guessed():
                self.__result = Result.WIN
        return was_correct

    def __handle_guess(self, ch):
        self.__nr_guesses += 1
        was_correct = self.__secret.handle_guess(ch)
        return was_correct

    # ----- Getters used by CLI ------------------------
    def get_nr_of_guesses(self) -> int:
        return self.__nr_guesses

    def get_result(self):
        return self.__result

    def is_over(self) -> bool:
        return self.__result != Result.NONE
