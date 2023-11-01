# package exercises.ex4hangman

# Representing the man
class Man:
    def __init__(self):
        self.nr_incorrect_guesses = 0

    def increment_hanging(self) -> None:
        self.nr_incorrect_guesses += 1

    def is_hung(self) -> bool:
        return self.nr_incorrect_guesses >= len(Man.parts)

    def __str__(self):
        return "".join(Man.parts[:self.nr_incorrect_guesses])

    # ------------- Helpers and graphics --------------------------
    # Parts of the hanging man (NL is the new line character, don't need to understand)
    NL = "\n"
    parts = [
        "---|" + NL,
        "   |" + NL,
        "   O" + NL,
        "  /",
        "|",
        "\\" + NL,
        "  /",
        " \\" + NL,
    ]

