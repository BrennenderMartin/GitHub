package Sudoku;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class reading_csv {
    public static void main(String[] args) {
        new reading_csv("matrix.csv");
    }

    public reading_csv(String path) {
        File csvFile = new File(path); // Pfad zur CSV-Datei
        ArrayList<int[]> matrixList = new ArrayList<>(); // Liste für Zeilen der Matrix

        read_csv(csvFile, matrixList);

        // ArrayList in 2D-Array (Matrix) umwandeln
        int[][] matrix = matrixList.toArray(new int[matrixList.size()][]);

        System.out.println("Matrix aus der CSV-Datei:");

        print_csv(matrix);

        //delete_csv(csvFile);
    }

    public static int[][] read_csv(String path) {
        File csvFile = new File(path); // Pfad zur CSV-Datei
        ArrayList<int[]> matrixList = new ArrayList<>(); // Liste für Zeilen der Matrix

        read_csv(csvFile, matrixList);

        // ArrayList in 2D-Array (Matrix) umwandeln
        int[][] matrix = matrixList.toArray(new int[matrixList.size()][]);

        return matrix;
    }

    public static <T> T read_csv(Class<T> type, String path) {
        File csvFile = new File(path); // Pfad zur CSV-Datei
        ArrayList<int[]> matrixList = new ArrayList<>(); // Liste für Zeilen der Matrix

        read_csv(csvFile, matrixList);

        // ArrayList in 2D-Array (Matrix) umwandeln
        int[][] matrix = matrixList.toArray(new int[matrixList.size()][]);


        // Konvertierte ArrayList<ArrayList<Integer>>
        ArrayList<ArrayList<Integer>> arrayListOfLists = new ArrayList<>();
        
        // Konvertierung durchführen
        for (int[] array : matrixList) {
            ArrayList<Integer> innerList = new ArrayList<>();
            for (int value : array) {
                innerList.add(value); // Werte aus int[] in ArrayList<Integer> hinzufügen
            }
            arrayListOfLists.add(innerList);
        }

        // Ergebnis anzeigen
        System.out.println("Original ArrayList<int[]>:");
        for (int[] array : matrixList) {
            System.out.println(Arrays.toString(array));
        }

        if (type == ArrayList.class) {
            return type.cast(arrayListOfLists);
        } else if (type == int[][].class) {
            return type.cast(matrix);
        } else {
            throw new IllegalArgumentException("Unsupported type: " + type.getName());
        }
    }

    public static void read_csv(File csvFile, ArrayList<int[]> matrixList) {
        // CSV-Datei einlesen
        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Zeile in Werte aufteilen
                String[] values = line.split(",");
                // Werte in int[] umwandeln
                int[] row = new int[values.length];
                for (int i = 0; i < values.length; i++) {
                    row[i] = Integer.parseInt(values[i]);
                }
                matrixList.add(row); // Zeile zur Matrix hinzufügen
            }
        } catch (IOException e) {
            System.err.println("Fehler beim Einlesen der Datei: " + e.getMessage());
            return;
        }
    }

    public static void print_csv(int[][] matrix) {
        // Matrix ausgeben
        for (int[] row : matrix) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }

    public static void delete_csv(File csvFile) {
        // CSV-Datei löschen
        if (csvFile.delete()) {
            System.out.println("Die Datei wurde erfolgreich gelöscht.");
        } else {
            System.err.println("Die Datei konnte nicht gelöscht werden.");
        }
    }
}
