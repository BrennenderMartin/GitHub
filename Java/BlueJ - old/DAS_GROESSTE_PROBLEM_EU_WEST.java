
/**
 * Write a description of class DAS_GROESSTE_PROBLEM_EU_WEST here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */

import java.util.Scanner;
public class DAS_GROESSTE_PROBLEM_EU_WEST
{
    

    /**
     * Constructor for objects of class DAS_GROESSTE_PROBLEM_EU_WEST
     */
    public DAS_GROESSTE_PROBLEM_EU_WEST()
    {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib eine Zahl ein:");
            int zahl = scanner.nextInt();
            int counter = 0;
            while(zahl != 1)
            {
                if(zahl % 2 == 0)
                {
                    zahl = zahl / 2;
                } else 
                {
                    zahl = zahl * 3 + 1;
                }
                System.out.println(zahl);
                counter++;
            }
            System.out.println("Anzahl benötigte Durchgänge: " + counter);
        }
    }

    
}
