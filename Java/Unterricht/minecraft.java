import java.util.Scanner;

public class minecraft {
    static int leben = 20;
    static int hunger = 20;

    String[] hotbar = new String[9];

    public static void main(String[] args) {
        new minecraft();
    }

    public minecraft() {
        hotbar_output();
        main();
        hotbar_output();
    }
    
    private void hotbar_output() {
        for(int i = 0; i < 9; i++) {
            System.out.println(hotbar[i]);
        }
        System.out.println(" ");
    }

    private void main() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hallo, wie heißt du?");

        String name = scanner.nextLine();
        System.out.println("Hallo " + name + " Du hast gerade " + leben / 2 + " Leben und " + hunger / 2 + " Hunger.");

        System.out.println("welchen Inventarplatz willst du wählen (1-9)?");
        int slot = scanner.nextInt();

        System.out.println("Was möchtest du im Inventar haben?");
        String item = scanner.nextLine();

        System.out.println("Dieses Item wird dir im Inventar hinzugefügt.");

        hotbar[slot - 1] = item;
        scanner.close();
    }

    private void test() {
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
}