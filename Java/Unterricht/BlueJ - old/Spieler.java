/**
 * Autor: Jan und Mattis
 * Klassenbeschreibung: ALADEEN
 */


//import vom Scanner (neue Bibliothek)
import java.util.Scanner;

//
public class Spieler
{
    //
    int muenzen;
    String name; 

    
    //
    public Spieler()
    {
        muenzen = 50;
        System.out.println("Gib deinen Namen ein: ");
        try (Scanner scanner = new Scanner(System.in)) {
            name = scanner.nextLine();
        }
    }
    
    
    //
    public void sageNamen()
    {
        System.out.println("Mein Name lautet: " + name);
    }
    
    public void sageMuenzen()
    {
        System.out.println(name + ": Ich habe noch " + muenzen + " Münzen.");
    }
}
