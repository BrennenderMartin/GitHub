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
    
    MyObject inputObject, outputObject;
    
    // Attribute
    String anschrift_name;
    String bestellungsname;
    String lieferadresse;

    String username;
    String password;
    
    int bestellung;
    
    // Konstruktor
    public CopyOfMamaMiaPizzaria() {
        fenster = new CopyOfDisplay("Pizzeria Traditore", this);
        start();
    }

    // Dienste
    public static void main(String[] args) { //Main used to launch an object
        @SuppressWarnings("unused")
        CopyOfMamaMiaPizzaria main = new CopyOfMamaMiaPizzaria();
    }

    public void fenster() {
        fenster.prompt("Name", "HungrigerTörke da Firenze");
        fenster.prompt("Passwort", "DeinPasswort");
        fenster.prompt("Bestellung", "Deportare Zaino"); // Abschieberucksack
        fenster.prompt("Lieferadresse", "Florenz");
    }

    public void fill_list() {
        // Alle Objekte der Speisekarte
        objectList.add(new MyObject("Deportare Zaino", 420.69));
        objectList.add(new MyObject("Pizza", 12.90));
        objectList.add(new MyObject("Pasta", 8.90));
        objectList.add(new MyObject("Pommes", 3.90));
    }

    public void start() {
        fenster();
        fill_list();
        
        bestellung = 0;
        while(bestellung < 10)
        {
            bestellung++;
            fenster.ready("Taste \"Bestellen\" drücken, wenn alle Werte eingeben. \n");
            anschrift_name = fenster.getString("Name");
            bestellungsname = fenster.getString("Bestellung");
            lieferadresse = fenster.getString("Lieferadresse");
            
            inputObject = new MyObject(bestellungsname);
            
            bestellen();
        }
    }

    public void bestellen() {
        fenster.println("Auftrag \"" + bestellungsname +
                        "\" für \"" + anschrift_name +
                        "\" in Bearbeitung nach \"" + lieferadresse +
                        "\". \n");
        
        if(objectList.contains(inputObject)) {
            for(int i = 0; i < objectList.size(); i++) { if(inputObject.getName().equals(objectList.get(i).getName())){outputObject = objectList.get(i);} }
            if(bestellungsname.equals("Deportare Zaino")) {
                fenster.println("Du kleiner Törke du! Tss tss tss...\n" +
                                "Zu faul etwas einzugeben? Tss tss tss...\n");
            } else { // Lässt nun das essen kochen
                fenster.println("Wird zubereitet...\n");
                
                kochen(bestellungsname);
                
            }
        } else {fenster.println("Tippfehler oder nicht auf der Karte, bitte neu bestellen\n");}
    }
    
    public void kochen(String bestellungsname) {
        fenster.println("Am kochen (" + bestellungsname + ") ...");
        // An Koch weitergeben
        fenster.println("Das macht " + outputObject.getAttribute() + "0€ bitte! \n");
    }
    
    public void login() {
        new StartFrame();
        User user = new User(username, password);
        System.out.println(user);
    }

    public void speisekarte() {
        fenster.println("Speisekarte:");
        int index = 1;
        for(MyObject myobject : objectList)
        {
            fenster.println(index + ". " + myobject.getName() + ", Preis: " + myobject.getAttribute());
            index++;
        }
        fenster.println(" ");
    }
    
    public void bezahlen() {
        bestellung--;
        fenster.println("Vielen Dank für Ihren Einkauf!");
        fenster.println("Der Bezahlvorgang ist abgeschlossen. \n");
    }

    @Override
    public String toString() { //Eig macht das nicht aber kb das zu löschen und wenn ich das mal verstehe kann das glaub ich mega gut sein
        return "Hurensohn";
    }
}
