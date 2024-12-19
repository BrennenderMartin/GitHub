
/**
 * Write a description of class Aufgaben_Heute here.
 *
 * @author Luis und Mattis
 * @version 1.0 /// 11.11.2024
 */

import java.util.Scanner;

public class Aufgaben_Heute
{
    Scanner scanner = new Scanner(System.in);
    boolean eingeloggt;
    boolean div_3;
    boolean div_5;

    /**
     * Constructor
     */
    public Aufgaben_Heute()
    {
        // initialise instance variables
        eingeloggt = false;
        div_3 = false;
        div_5 = false;
        einloggen();
    }

    /**
     *Methodes
     */
    public void einloggen()
    {
        // Lese eine Zeichenkette (ein Wort) ein
        System.out.print("Gib eine Aufgabe ein, welche bearbeitet werden soll: ");
        String input_name = scanner.nextLine();
        
        if(input_name.equals("a"))
        {
            eingeloggt = true;
            aufgabe_a();
        }else if(input_name.equals("b"))
        {
            eingeloggt = true;
            aufgabe_b();
        }else if(input_name.equals("c"))
        {
            eingeloggt = true;
            aufgabe_c();
        }else if(input_name.equals("d"))
        {
            eingeloggt = true;
            aufgabe_d();
        }else if(input_name.equals("e"))
        {
            eingeloggt = true;
            aufgabe_e();
        }else if(input_name.equals("f"))
        {
            eingeloggt = true;
            aufgabe_f();
        } else{
            System.out.println("Falscher Aufgabentyp du Bombenleger");
        }
        
        
        
    }
    
    public void aufgabe_a()
    {
        System.out.print("Gib eine Zahl ein: ");
        int input = scanner.nextInt();
        
        if(input == 10)
        {
           System.out.println("Die Zahl ist 10"); 
        } else if(input > 10)
        {
            System.out.println("Die Zahl ist größer als 10");
        } else {
            System.out.println("Die Zahl ist kleiner als 10");
        }
    }
    
    public void aufgabe_b()
    {
        for (int j = 1; j <= 10; j++) 
        {
            System.out.println("j ist: " + j);
        }
    }
    
    public void aufgabe_c()
    {
        for (int j = 2; j <= 50; j += 2) 
        {
            System.out.println("j ist: " + j);
        }
    }
    
    public void aufgabe_d()
    {
        for (int j = 1; j <= 11; j++) 
        {
            if(j == 3)
            {
                System.out.println("Keine Zahl du HUSO!");
            } else {
                System.out.println("j ist: " + j);
            }
        }
    }
    
    public void aufgabe_e()
    {
        for (int j = 1; j <= 30; j++)
        {
            if(j % 3 == 0)
            {
                System.out.println("Durch 3 Teilbar");
            } else {
                System.out.println("j ist: " + j);
            }
        }
    }
    
    public void aufgabe_f()
    {
        for (int j = 1; j <= 30; j++)
        {
            if(j % 3 == 0)
            {
                div_3 = true;
            } 
            if(j % 5 == 0)
            {
                div_5 = true;
            }
            if(div_3 == true && div_5 == true)
            {
                System.out.println("Teilbar 3 und 5");
            }
            if(div_3 == true)
            {
                System.out.println("Teilbar 3 ");
            }
            if(div_5 == true)
            {
                System.out.println("Teilbar 5");
            }
            if(div_3 == false || div_5 == false)
            {
                System.out.println("j ist: " + j);
            }
            div_3 = false;
            div_5 = false;
        }
    }
}
