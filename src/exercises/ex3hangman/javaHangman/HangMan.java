package exercises.ex3hangman.javaHangman;

/*
#  The Hangman game (in a text version)
#  This is the game logic
#
#  This illustrated the concept of an "OO-model" (i.e. many connected
#  objects from different classes). Objects working together to solve a problem.
*/

public class HangMan {
    // TODO instance attributes must be declared here

    // Inner class, no need to understand details.
    // Accessed as HangMan.Result.NONE etc.
    public enum Result {
        NONE,
        WIN,
        LOSE
    }

    public HangMan(Man man, Secret secret) {
        // TODO
    }

    // The game logic
    public boolean update(char ch) {
        // TODO
        return false;
    }

    private boolean handleGuess(char ch) {
        // TODO
        return false;
    }

    // ----- Getters used by CLI ------------------------
    public int getNrOfGuesses() {
        // TODO
        return 0;
    }

    public Result getResult() {
        // TODO
        return null;    // Like python's None
    }

    public boolean isOver() {
        // TODO
        return false;
    }
}