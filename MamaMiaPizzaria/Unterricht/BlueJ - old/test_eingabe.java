
/**
 * Write a description of class test_eingabe here.
 *
 * @author Ikke
 * @version 02.12.2024
 */

import java.util.Scanner;
public class test_eingabe
{
    int x;
    
    /**
     * Constructor for objects of class test_eingabe
     */
    public test_eingabe()
    {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib eine Zahl ein:");
            x = 2;
            exe(scanner.nextInt());
        }
    }

    public void exe(int y)
    {
        System.out.println("Die Zahl verdoppelt ist: " + y * x);
    }
}
