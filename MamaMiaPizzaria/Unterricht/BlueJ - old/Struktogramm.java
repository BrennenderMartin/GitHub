
/**
 * Struktogramm Aufgabe pdf Datei.
 *
 * @Mattis
 * @18.11.2024 // 1.0
 */
import java.util.Scanner;
import java.util.Random;
public class Struktogramm
{
    // instance variables - replace the example below with your own
    int raten;
    int eingabe;
    int zaehler;
    boolean run;

    /**
     * Constructor for objects of class Struktogramm
     */
    public Struktogramm()
    {
        // initialise instance variables
        Random rand = new Random();
        raten = rand.nextInt(100);
        //System.out.println(raten);
        eingabe = 0;
        zaehler = 0;
        run = true;
        while(run)
        {
            try (Scanner scanner = new Scanner(System.in)) {
                System.out.println("Rate die richtige Zahl! ");
                eingabe = scanner.nextInt();
            }
            if(eingabe == raten)
            {
                System.out.println("Richtig!");
                run = false;
            } else if(eingabe == 101){
                System.out.println("Die Zahl war: " + raten);
                run = false;
            } else {
                if(raten < eingabe)
                {
                    System.out.println("Zu groß du scheiß Arschkrampenvieh");
                } else {
                    System.out.println("Zu klein du dumme Orgasmusbremse");
                }
            }
            zaehler++;
        }
        System.out.println("Du hast " + zaehler + " Versuche gebraucht");
    }

}
