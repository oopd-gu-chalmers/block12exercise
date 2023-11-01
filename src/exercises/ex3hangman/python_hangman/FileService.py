# package exercises.ex4hangman;
from abc import ABC  # ABC = Abstract Base Class
from random import choice
import os.path as p


# File handling for Hangman
#
# Used to read file word.txt containing words to guess.
#
#     *** Nothing to do here ***
# The FileService is declared *abstract*, by inheriting ABC,
# meaning we cannot construct instances of it.
class FileService(ABC):
    @staticmethod
    def get_random_word_from_file(path_list):
        path = p.join(path_list)
        words = FileService.read_file(path)
        the_word = choice(words)
        return the_word

    @staticmethod
    def read_file(path):
        # Use with resource to ensure stream is closed
        with open(path, 'rt', encoding='utf-8') as file_reader:
            lines = []
            while (line := file_reader.readline()) != '':
                lines.append(line.strip('\n'))
            return lines
