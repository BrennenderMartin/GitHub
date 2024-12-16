
/**
 * Beschreiben Sie hier die Klasse Level1.
 * 
 * @author (Ihr Name) 
 * @version (eine Versionsnummer oder ein Datum)
 */

import java.util.Scanner;

public class Level3
{
    // Instanzvariablen - ersetzt Variablen und sichert Speicherplatz, z.B. "int x;", x ist dann dafür da, Zahlen zu Speichern. 
    String benutzername;
    String passwort;

    //Konstruktor, wird beim Erstellen der Klasse ausgeführt. 
    //Wird meist genutzt, um Instanzvariablen zu initialisieren, also werte zuzuweisen wie "x=3;". x hat dann den Wert 3 gespeichert
    public Level3()
    {
        // Instanzvariable initialisieren
        String eingabeName;
        try (Scanner robin = new Scanner(System.in)) {
            eingabeName = robin.nextLine();
            
            if(eingabeName.equals(benutzername)){
                System.out.println("Name korrekt, bitte Passwort eingeben");
                String eingabePasswort;
                eingabePasswort = robin.nextLine();
                if(eingabePasswort.equals(passwort)){
                    System.out.println("Passwort korrekt, willkommen " + benutzername);
                }
                else
                {
                    System.out.println("Falsches Passwort");
                }
            }
            else
            {
                System.out.println("Falscher Nutzername");
            }
        }
    }
    
    
    //Für Später! 
    //Methoden, können aufgerufen werden, um Variablen zu verändern oder etwas zu berechnen oder auszugeben
    public void multipliziere(int x, int y)  //aufrufbar im Konstruktor mit: multipliziere(4, 6); 
    {
        int produkt; 
        produkt = x * y;
        System.out.println("Das Produkt von " + x + " und " + y + " lautet " + produkt);
    }
    
    public int addiere(int x, int y)          //aufrufbar im Konstruktor mit: addiere(3, 5); 
    {
        int summe = x+y;
        return summe;
    }
}
