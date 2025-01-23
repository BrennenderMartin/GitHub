package Blackjack;

/**
 * @author 
 * @version 
 */
public class Card
{
    // Bezugsobjekte
    String color;
    String m;
    String value;
    String l;
    // Attribute

    // Konstruktor
    public Card(int n, int k) {
        switch (n) {
            case 1: m = "Diamonds"; break;
            case 2: m = "Hearts"; break;
            case 3: m = "Spades"; break;
            case 4: m = "Clubs"; break;
            default: System.out.println("Vwong numbah");
        }

        switch (k) {
            case 1: l = "Ace"; break;
            case 2: l = "2"; break;
            case 3: l = "3"; break;
            default: System.out.println("wong numbah");
        }
        color = m;
        value = l;
    }
    
    // Dienste
    public void setColor(String imp_color) {
        color = imp_color;
    }

    public void setValue(String imp_value) {
        value = imp_value;
    }
    public String getColor() {
        return color;
    }

    public String getValue() {
        return value;
    }
}
