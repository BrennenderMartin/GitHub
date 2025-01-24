package Blackjack;

public class Card {
    public static String color;
    public int n;
    String m;

    public static String value;
    public int k;
    String l;

    public Card(int n, int k) {

        this.n = n;
        this.k = k;

        switch (n) {
            case 1: m = "Diamonds"; break;
            case 2: m = "Hearts"; break;
            case 3: m = "Spades"; break;
            case 4: m = "Clubs"; break;
            default: System.out.println("wong numbah");
        }

        switch (k) {
            case 1: l = "Ace"; break;
            case 2: l = "2"; break;
            case 3: l = "3"; break;
            case 4: l = "4"; break;
            case 5: l = "5"; break;
            case 6: l = "6"; break;
            case 7: l = "7"; break;
            case 8: l = "8"; break;
            case 9: l = "9"; break;
            case 10: l = "10"; break;
            case 11: l = "Jack"; break;
            case 12: l = "Queen"; break;
            case 13: l = "King"; break;
            default: System.out.println("wong numbah");
        }
        
        color = m;
        value = l;
    }
    
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
