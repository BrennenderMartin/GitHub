/**
 * @author Name
 * @version 
 */

import java.util.Scanner;

public class LogIn
{
    // Attribute
    String name; 
    int pw;
    int counter;
    Scanner scanner = new Scanner(System.in);

    // Konstruktor
    public LogIn()
    {
        name = "asdf";
        pw = 1234; 
        einloggen();
    }
    
    public void wrong_user()
    {
        // Lese eine Zeichenkette (ein Wort) ein
        System.out.print("Gib den Nutzer ein: ");
        String input_name = scanner.nextLine();
        
        System.out.print("Gib das Passwort ein: ");
        int input_pw = scanner.nextInt();

        if(input_name.equals(name))
        {
            if(input_pw == pw)
            {
                System.out.println("Du bist drin");
            }
            else
            {
                wrong_pw();
            }
        }
        else
        {
            System.out.println("Bist du dumm??!??!??");
        }
    }
    
    public void wrong_pw()
    {
        //try again for 5 times
        while (counter < 5)
        {
            counter++;
            System.out.print("Gib das Passwort ein: ");
            int input_pw = scanner.nextInt();
            
            if (input_pw == pw)
            {
                System.out.println("Du bist drin");
                break;
            }
        }
    }
    // Dienste
    /* Aufgabe: Beim Aufrufen der Funktion einloggen soll der Nutzer 
     * den richtigen Login Namen und das richtige Passwort eingeben. 
     * Wenn eine Sache falsch eingegeben wurde, kommt eine Fehlermeldung. 
     */
    public void einloggen()
    {

        // Lese eine Zeichenkette (ein Wort) ein
        System.out.print("Gib den Nutzer ein: ");
        String input_name = scanner.nextLine();
        
        System.out.print("Gib das Passwort ein: ");
        int input_pw = scanner.nextInt();

        if(input_name.equals(name))
        {
            if(input_pw == pw)
            {
                System.out.println("Du bist drin");
            }
            else
            {
                wrong_pw();
            }
        }
        else
        {
            System.out.println("Schwul");
            
        }
    }
}
