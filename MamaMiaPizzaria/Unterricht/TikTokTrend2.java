package Unterricht;
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
    public void trend()
    {
        int zahl = 0;
        int max_operations = 0;
        for(int i = 2; i <= 100000; i++) {
            int counter = 0;
            zahl = i;
            System.out.println("Prüfe die Zahl " + zahl);
        
            while (zahl != 1)
            {
                counter++;
                if( zahl%2 == 0 )   //Gerade
                {
                    zahl /= 2;
                }
                else                //Ungerade
                {
                    zahl *= 3;
                    zahl++;
                }
                //System.out.println(zahl); //Solltest du auskommentieren!
                if(counter > max_operations) {
                    max_operations = i;
                }
            }

        }
        System.out.println(max_operations);
    }

}
