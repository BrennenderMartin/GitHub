
import java.util.Scanner;

/**
 * Just a small programm, because Java is
 * alwasy taking ages to get running, so
 * you can just let it run this file, and
 * if it runs, you know everything is set
 * up accordingly and you can start coding! :)
 */

public class alphatest {
    public static void main(String[] args) {
        System.out.println("\nFinal tests complete... Ready to run any Programms in Java! :) \n");
    }

    @SuppressWarnings("unused")
    private int scanner() {
        int var;
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("text");
            var = scanner.nextInt();
        }
        return var;
    }

}
