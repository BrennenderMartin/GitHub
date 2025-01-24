package Unterricht;

public class threading {
    public static void main(String[] args) {
        // Thread für Person A
        Thread personA = new Thread(() -> {
            for (int i = 1; i <= 10; i++) {
                System.out.println("Person A zählt: " + i);
            }
        });

        // Thread für Person B
        Thread personB = new Thread(() -> {
            for (int i = 1; i <= 10; i++) {
                System.out.println("Person B zählt: " + i);
            }
        });
        // Threads starten
        personA.start();
        personB.start();
        while(personA.isAlive() | personB.isAlive()) {
            if (!personA.isAlive()){
                System.out.println("Person A finished");
            } else if(!personB.isAlive()) {
                System.out.println("Person B finished");
            }
        }
    }
}
