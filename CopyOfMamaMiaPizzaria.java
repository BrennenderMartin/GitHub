import java.util.ArrayList;
import java.util.List;
/**
 * Die Pizzeria
 * 
 * @author: base made by Fischi, edited by Luis and Mattis
 */
public class CopyOfMamaMiaPizzaria
{
    // Bezugsobjekte
    CopyOfDisplay fenster;
    //private CopyOfDisplay fenster;
    
    // Liste von Objekten erstellen
    List<MyObject> objectList = new ArrayList<>();
    
    MyObject inputObject;
    
    // Attribute
    String anschrift_name;
    String bestellungsname;
    String lieferadresse;
    
    int bestellung;
       
    // Konstruktor
    public CopyOfMamaMiaPizzaria()
    {
        fenster = new CopyOfDisplay("Pizzeria Traditore", this);
        fenster.prompt("Name", "HungrigerTörke da Firenze");
        fenster.prompt("Bestellung", "Deportare Zaino"); // Abschieberucksack
        fenster.prompt("Lieferadresse", "Florenz");
        
        // Alle Objekte der Speisekarte
        objectList.add(new MyObject("Deportare Zaino", 69.69));
        objectList.add(new MyObject("Pizza", 12.90));
        objectList.add(new MyObject("Pasta", 8.90));
        objectList.add(new MyObject("Pommes", 3.90));
        
        bestellung = 0;
        while(bestellung < 10)
        {
            bestellung++;
            fenster.ready("Taste \"Bestellen\" drücken, wenn alle Werte eingeben.");
            anschrift_name = fenster.getString("Name");
            bestellungsname = fenster.getString("Bestellung");
            lieferadresse = fenster.getString("Lieferadresse");
            
            inputObject = new MyObject(bestellungsname);
            
            exe();
        }
    }
    
    public static void main(String[] args)
    { 
        CopyOfMamaMiaPizzaria object = new CopyOfMamaMiaPizzaria();
        System.out.println(object);
    }
    
    // Dienste
    public void exe()
    {
        fenster.println("Auftrag \"" + bestellungsname + 
                        "\" für \"" + anschrift_name + 
                        "\" in Bearbeitung nach \"" + lieferadresse + 
                        "\".");
        
        if (objectList.contains(inputObject)) {
            if(bestellungsname.equals("Deportare Zaino")){
            
                fenster.println("Du kleiner Törke du! Tss tss tss...");
                fenster.println("Zu faul etwas einzugeben? Tss tss tss...");
            
            } else { // Lässt nun das essen kochen
                
                fenster.println("Wird zubereitet...");
                
                kochen(bestellungsname);
                
            }
        } else { // Error Meldung 
            
            fenster.println("Tippfehler oder nicht auf der Karte, bitte neu bestellen");
            
        }
    }
    
    public void kochen(String bestellungsname)
    {
        fenster.println("Am kochen (" + bestellungsname + ") ...");
        // An Koch weitergeben
        fenster.println("Das macht 35 € bitte! ");
        bestellung--;
    }
    
    public void speisekarte()
    {
        fenster.println("Speisekarte:");
        int index = 1;
        for(MyObject myobject : objectList)
        {
            fenster.println(index + 
                            ". " + myobject.getName() + 
                            ", Preis: " + myobject.getAttribute());
        }
        // Gibt die Speisekarte im Display aus
    }
    
    public void bezahlen()
    {
        fenster.println("Vielen Dank für Ihren Einkauf!");
        fenster.println("Der Bezahlvorgang ist abgeschlossen.");
    }

    @Override
    public String toString() {
        return "Hurensohn";
    }
}
