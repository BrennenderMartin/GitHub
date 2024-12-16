
/**
 * Write a description of class tannenbaum_erstellen here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class tannenbaum_erstellen
{
    // instance variables - replace the example below with your own
    int height;
    int a;
    int x;
    int width;
    int j;
    int i;
    String text;
    String text1;
    String text2;
    String text3;

    /**
     * Constructor for objects of class tannenbaum_erstellen
     */
    public tannenbaum_erstellen()
    {
        try (// initialise instance variables
        Scanner scanner = new Scanner(System.in)) {
            System.out.println("Wie hoch: ");
            height = scanner.nextInt();
        }
        a = 1;
        j = 0;
        i = 0;
        width = a + height * 2;
        text = "";
        text1 = "";
        text2 = "";
        text3 = "";
        x = 0;
        exe2();
    }
    
    public void exe2()
    {
        for(int j = 2; j <= 20; j += 2){System.out.println(j);}
    }
    
    public void exe_whyle()
    {
        while(j <= height + 3)
        {
            if(j == 0)
            {
                while(i < width)
                {
                    text += "_";
                    i++;
                }
                System.out.println(text);
                text = "";
            } else if(j > 0 && j < height + 1)
            {
                x = 0;
                a = 1;
                a += (2 * j) - 2;
                int colwidth = (width - a) / 2;
                while(x < a)
                {
                    if(x % 2 == 0)
                    {
                        text2 += "X";
                    } else 
                    {
                        text2 += "O";
                    }
                    x++;
                }
                x = 0;
                while(x < colwidth)
                {
                    text1 += "_";
                    text3 += "_";
                    x++;
                }
                
                text = text1 + text2 + text3;
                System.out.println(text);
                text = "";
                text1 = "";
                text2 = "";
                text3 = "";
            } else if(j == height + 2)
            {
                x = 0;
                a = 1;
                int colwidth = width / 2;
                text2 += "O";
                x = 0;
                while(x < colwidth)
                {
                    text1 += "_";
                    text3 += "_";
                    x++;
                }
                
                text = text1 + text2 + text3;
                System.out.println(text);
                text = "";
                text1 = "";
                text2 = "";
                text3 = "";
            }else if(j == height + 3)
            {
                while(i < width)
                {
                    text += "_";
                    i++;
                }
                System.out.println(text);
                text = "";
            }
            j++;
        }
    }
    
    public void exe()
    {
        for(int j = 0; j <= height + 3; j++)
        {
            if(j == 0)
            {
                for(int i = 0; i < width; i++)
                {
                    text += "_";
                }
                System.out.println(text);
                text = "";
            } else if(j > 0 && j < height + 1)
            {
                x = 0;
                a = 1;
                a += (2 * j) - 2;
                int colwidth = (width - a) / 2;
                while(x < a)
                {
                    if(x % 2 == 0)
                    {
                        text2 += "X";
                    } else 
                    {
                        text2 += "O";
                    }
                    x++;
                }
                x = 0;
                while(x < colwidth)
                {
                    text1 += "_";
                    text3 += "_";
                    x++;
                }
                
                text = text1 + text2 + text3;
                System.out.println(text);
                text = "";
                text1 = "";
                text2 = "";
                text3 = "";
            } else if(j == height + 2)
            {
                x = 0;
                a = 1;
                int colwidth = width / 2;
                text2 += "O";
                x = 0;
                while(x < colwidth)
                {
                    text1 += "_";
                    text3 += "_";
                    x++;
                }
                
                text = text1 + text2 + text3;
                System.out.println(text);
                text = "";
                text1 = "";
                text2 = "";
                text3 = "";
            }else if(j == height + 3)
            {
                for(int i = 0; i < width; i++)
                {
                    text += "_";
                }
                System.out.println(text);
                text = "";
            }
        }
    }
}
