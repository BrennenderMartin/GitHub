package Unterricht;

import java.util.Scanner;

public class minecraft {
    int leben = 20;
    int hunger = 20;

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
        System.out.println("Hier sind alle Inventarslots:");
        for (int i = 0; i < 9; i++) {
            System.out.println((i + 1) + ". " + hotbar[i]);
        }
        System.out.println(" ");
    }

    private void main() {
        Scanner scStr = new Scanner(System.in);
        Scanner scInt = new Scanner(System.in);

        System.out.println("Hallo, wie heißt du?");

        String name = scStr.nextLine();
        System.out.println("Hallo " + name + " Du hast gerade " + leben / 2 + " Leben und " + hunger / 2 + " Hunger.");

        System.out.println("welchen Inventarplatz willst du wählen (1-9)?");
        int slot = scInt.nextInt();

        System.out.println("Was möchtest du im Inventar haben?");
        String item = scStr.nextLine();
        hotbar[slot - 1] = item;

        System.out.println("Dieses Item (" + item + ") wird dir im Inventar hinzugefügt.");
        
        scStr.close();
        scInt.close();
    }
}