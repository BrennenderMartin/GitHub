package HerrLinden;

import java.util.Scanner;
/*
 *  try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib mir eine Zahl zwischen 1 und " + max + " und ich errate diese: ");
            var = scanner.nextInt();
        }
 */
public class programmcopy {
    int start = 0;
    int end = 0;
    String function;
    public static void main(String[] args) {
        new programmcopy();
    }

    public programmcopy() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib den Anfang der Range an: ");
            function = scanner.nextLine();
            System.out.println("Gib den Anfang der Range an: ");
            start = scanner.nextInt();
            System.out.println("Gib das Ende der Range an: ");
            end = scanner.nextInt();
        }
        System.out.println("Start: " + start + " End: "+ end);
        
        if (start != 0 && end != 0) {
            System.out.println(get_area(start, end));
        } else {
            System.out.println("Funktioniert nicht");
        }
    }

    public float calc_function(float x) {
        String func = function.replace("x", x);
        float y = x * x;

        return y;
    }

    public float get_height(int start, int end) {
        float value = 0;
        float i = start;
        int counter = 0;

        while(i <= end) {
            value += calc_function(i);
            //System.out.println(i);
            i += 0.1;
            counter++;
        }
        value = value / counter;
        value = Math.round(value);
        return value;
    }

    public float get_width(int start, int end) {
        return end - start;
    }

    public float get_area(int start, int end) {
        return get_height(start, end) * get_width(start, end);
    }
}