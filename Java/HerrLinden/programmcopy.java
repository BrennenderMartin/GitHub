package HerrLinden;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

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
    String eval_funct;
    public static void main(String[] args) {
        new programmcopy();
    }

    public static String convertFloatToString(float floatValue) {
        String stringValue = "" + floatValue;
        return (stringValue);
    }

    public programmcopy() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib die Funktion an: ");
            function = scanner.nextLine();
            System.out.println("Gib den Anfang des Intervalls an: ");
            start = scanner.nextInt();
            System.out.println("Gib das Ende des Intervalls an: ");
            end = scanner.nextInt();
        }
        System.out.println("Start: " + start + " End: "+ end);
        
        System.out.println(get_area(start, end));
        
    }

    public void create_function(String function) {
        char[] chars = new char[function.length()];
        String[] strings = new String[function.length()];
        for (int i = 0; i < function.length(); i++){
            chars[i] = function.charAt(i);
            strings[i] = String.valueOf(chars[i]); 
            
        }
    }

    public double function(float x) {
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("js");

        eval_funct = function.replace("x", convertFloatToString(x));

        Object y;
        try {
            y = engine.eval(eval_funct);
            return (double) y;
        } catch (ScriptException e) {
            e.printStackTrace();
            return 0.0;
        }
    }
    
    public double integral_calc(int start, int end) {
        double y = function(0);
        String derivation = eval_funct;

        return y;
    }

    public float get_height(int start, int end) {
        float value = 0;
        float i = start;
        int counter = 0;

        while(i <= end) {
            value += function(i);
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