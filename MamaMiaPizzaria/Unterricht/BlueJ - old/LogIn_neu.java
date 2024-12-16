
/**
 * Write a description of class LogIn_neu here.
 *
 * @author Luis, Mattis und als Motivation und Ablenkung noch robin
 * @version 1.0 /// 07.11.2024
 */

import java.util.Scanner;
import static java.lang.Math.sqrt;

public class LogIn_neu
{
    // Attribute
    String name; 
    String pw;
    int counter;
    int vv;
    boolean eingeloggt;
    double p;
    double q;
    double p_2;
    double rest;
    Scanner scanner = new Scanner(System.in);

    /**
     * Constructor for objects of class LogIn_neu
     */
    public LogIn_neu()
    {
        name = "asdf";
        pw = "1234";
        eingeloggt = false;
        einloggen();
        
        if (eingeloggt)
        {
            pqformel();
        }

    }
    
    public void pqformel()
    {
        System.out.println("Gebe das p ein: ");
        double p = scanner.nextDouble();
        
        System.out.println("Gebe das q ein: ");
        double q = scanner.nextDouble();
        
        System.out.println("x^2" + "+" + p + "x" + "+" + q);
        
        p_2 = - (p / 2);
        rest = sqrt((p_2 * p_2) - q);
        
        System.out.println(-p_2 + rest);
        System.out.println(-p_2 - rest);
        
    }
    
    public void einloggen()
    {
        // Lese eine Zeichenkette (ein Wort) ein
        System.out.print("Gib den Nutzer ein: ");
        String input_name = scanner.nextLine();
        
        if(input_name.equals(name))
        {
            while(counter < 5)
            {
                vv = 5 - counter;
                System.out.println("Remaining tries: " + vv);
                System.out.print("Gib das Passwort ein: ");
                String input_pw = scanner.nextLine();
                
                if(input_pw.equals(pw))
                {
                    System.out.println("Du bis drin");
                    counter += 10;
                    eingeloggt = true;
                }
                else
                {
                    System.out.println("Falsches Passwort du Törken-Abschieberucksack-Fresser!" );
                    counter++; 
                }
            }
        }
        else
        {
            System.out.println("msg");
        }
    }
}
