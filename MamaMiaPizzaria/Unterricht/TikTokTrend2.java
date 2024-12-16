// TikTokTrend:
// Eine Zahl kann immer zur 1 umgeformt werden!
// Dazu muss man nur folgende Rechnungen durchführen:
// wenn sie gerade ist: mit 2 dividieren
// wenn sie ungerade ist: mit 3 multipliziert und +1 addiert,

public class TikTokTrend2
{
    // Instanzvariablen deklarieren

    // Konstruktor
    public TikTokTrend2()
    {
        /*Prüfe, ob der TikTok-Trend für die Zahlen von 2 bis 100 stimmt. */
        
        trend();
        
        //Erweiterung:
        //Für die Zahlen von 2 bis 1000 - bei welcher Zahl müssen am meisten Rechnungen durchgeführt werden?
    }

    public static void main(String[] args) {
        @SuppressWarnings("unused")
        TikTokTrend2 main = new TikTokTrend2();
    }
    
    // Code von letzter Woche:
    public void trend() {

        int zahl = 0;
        int max_op = 0;
        int min_op = 420;

        int max_co = 0;
        int min_co = 0;

        for(int i = 2; i <= 1000; i++) {
            int counter = 0;
            zahl = i;
            //System.out.println("Prüfe die Zahl " + zahl);
        
            while (zahl != 1) {
                counter++;
                if( zahl % 2 == 0 ) {  //Gerade
                    zahl /= 2;
                } else {             //Ungerade
                    zahl *= 3;
                    zahl++;
                }
            }
            if(counter > max_op) {
                max_op = i;
                max_co = counter;
            }
            if(counter < min_op) {
                min_op = i;
                min_co = counter;
            }
        }
        System.out.println( " Größte Zahl: " + max_op +
                            " Anzahl Operationen: " + max_co);
        System.out.println( " Kleinste Zahl: " + min_op +
                            " Anzahl Operationen: " + min_co);
    }

}
