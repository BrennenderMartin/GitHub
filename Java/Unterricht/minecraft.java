import java.util.Scanner;

public class minecraft {
    static int leben = 20;
    static int hunger = 20;

    String[] hotbar = new String[9];
    

    public static void main(String[] args) {
        new minecraft();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hallo, wie heißt du?");

        String name = scanner.nextLine();
        System.out.println("Hallo " + name + " Du hast gerade " + leben / 2 + " Leben und " + hunger / 2 + " Hunger.");

        System.out.println("welchen Inventarplatz willst du wählen (1-9)?");
        int slot = scanner.nextInt();

        System.out.println("Was möchtest du im Inventar haben?");
        String item = scanner.nextLine();

        System.out.println("Du hast jetzt folgendes Item: " + item + " im " + slot + ". Slot");
        
        scanner.close();
    }

    minecraft() {
        for(int i = 0; i < 9; i++) {
            System.out.println(hotbar[i]);
        }
        
    }
}