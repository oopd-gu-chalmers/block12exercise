package exercises.ex2arrays;

public class Arrays {

    /* The input functions */
    public static int[] getArrayOfIntsFromUser() {
        // TODO
        return new int[5];
    }

    public static int getValueFromUser() {
        // TODO
        return 0;
    }

    /* The output functions */
    public static void printIndexToUser(int the_index, int the_value) {
        // TODO
    }

    public static void printNotFoundToUser(int the_value) {
        // TODO
    }

    public static void printResultToUser(int the_index, int the_value) {
        // TODO
    }


    /* The Algorithm */
    public static int findIndexOfValue(int[] a_list, int a_value) {
        // TODO
        return 0;
    }

    /* The top-level behavior */
    public static void listBasicsProgram() {
        // INPUT
        int[] theList = getArrayOfIntsFromUser();
        int theValue = getValueFromUser();
        // PROCESS
        int theIndex = findIndexOfValue(theList, theValue);
        // OUTPUT
        printResultToUser(theIndex, theValue);
    }


    /* Required way to make module executable */
    public static void main(String[] args) {
        listBasicsProgram();
    }
}
