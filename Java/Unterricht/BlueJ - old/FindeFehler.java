/**
 * @author: ein Programmieranfänger :)
 * @version 1, finde die Fehler, sodass sich das Programm ausführen lässt
 */

public class FindeFehler
{
    // Attribute
    int zahl1, zahl2;
    String text;
    
    
    // Konstruktor
    public FindeFehler()
    {
        text = "Mein Name ist "; 
        zahl1 = 7;
        zahl2 = 11;
        
        schreibeZahl();
        schreibeNamen();
    }

    // Methoden
    public void schreibeZahl()
    {
        int addiert; 
        addiert = zahl1 + zahl2;
        System.out.println(zahl1 + " + " + zahl2 + " = " + addiert); 
    }
    
    public void schreibeNamen()
    {
        System.out.println(text + "Philipp");
    }
}
