
/**
 * Erstelle ein bild aus Kreisen, nach inputs
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class Bild_erstellen
{
    // instance variables - replace the example below with your own
    int height;
    int width;
    String text;

    /**
     * Constructor for objects of class Bild_erstellen
     */
    public Bild_erstellen()
    {
        try (// initialise instance variables
        Scanner scanner = new Scanner(System.in)) {
            System.out.println("Wie hoch soll das bild sein: ");
            height = scanner.nextInt();
            System.out.println("Wie breit soll das bild sein: ");
            width = scanner.nextInt();
        }
        
        text = "";
        exe();
        
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void exe()
    {
        for(int j = 0; j < height; j++)
        {
            for(int i = 0; i < width; i++)
            {
                text += "O";
            }
            System.out.println(text);
            text = "";
        }
    }
}
