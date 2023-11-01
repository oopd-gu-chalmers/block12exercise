package exercises.ex3hangman.javaHangman;

// Representing the man
class Man {
    // instance variables are declared here
    int nrIncorrectGuesses;

    public Man() {
        // instance variables are often initialized here, but
        // must be declared outside, at the class level.
        this.nrIncorrectGuesses = 0;
    }

    public void incrementHanging() {
        this.nrIncorrectGuesses += 1;
    }

    public boolean isHung() {
        return this.nrIncorrectGuesses >= Man.parts.length;
    }

    @Override
    public String toString() {
        // TODO
        return "";
    }

    // ------------- Helpers and graphics --------------------------
    // Parts of the hanging man (NL is the new line character, don't need to understand)
    static final String NL = "\n";
    static final String[] parts = {
            "---|" + NL,
            "   |" + NL,
            "   O" + NL,
            "  /",
            "|",
            "\\" + NL,
            "  /",
            " \\" + NL,
    };
}
