import java.util.Arrays;

public class eva {
    public static void main(String[] args) {
        new eva();
    }
    
    eva() {
        aufgabe1();
        aufgabe2();
        aufgabe3();
        aufgabe4();
    }

    private void aufgabe1() {
        System.out.println("Aufgabe 1: ");
        int[] array = {1, 5, 10, 15, 20, 25, 30, 35};

        //a)
        System.out.println("Der Array hat: " + array.length + " Elemente.");

        //b)
        int gesuchterWert = 30;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == gesuchterWert) {
                System.out.println("Der gesuchte Wert (" + array[i] + ") steht an " + (i + 1) + ". Position im Array");
                break;
            }
        }

        //c)
        System.out.println(array[5]); // es wird der Wert an 4. Position ausgegeben, da der index bei 0 anfängt zu zählen
        System.out.println("");
    }

    private void aufgabe2() {
        System.out.println("Aufgabe 2: ");
        int array[] = new int[10];
        int summe = 0;

        for (int i = 0; i < 10; i++) {
            array[i] = i * 5;
        }
        System.out.println(Arrays.toString(array));

        for (int i = 0; i < 10; i++) {
            summe += array[i];
        }
        System.out.println("Die Summe aller Zahlen beträgt: " + summe);
        System.out.println("");
    }

    private void aufgabe3() {
        System.out.println("Aufgabe 3: ");
        int[] array = {12, 45, 7, 34, 89};
        int max = 0;

        for(int i = 0; i < array.length; i++) {
            if (array[i] >= max) {
                max = array[i];
            }
        }
        System.out.println("Das Maximum des Arrays ist: " + max);
        System.out.println("");
    }

    private void aufgabe4() {
        /*
         * 1. Der Hauptvorteil eines Arrays gegenüber einer Variable ist, 
         *    dass man in einem Array mehrere Werte gleichzeitig speichern kann und in einer Variable nicht
         * 
         * 2. Das 1. Element kann man mit array[0] aufrufen und das letze mit array[array.length - 1] Beispiel:
         */
        System.out.println("Aufgabe 4: ");
        int[] array = {1, 2, 3, 4};
        System.out.println("Erstes Element: " + array[0]);
        System.out.println("Letzes Element: " + array[array.length - 1]);
        System.out.println("");
    }
}
