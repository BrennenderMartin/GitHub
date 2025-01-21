package Sudoku;

public class test {
    public static void main(String[] args) {
        int[][] matrix = reading_csv.read_csv("matrix1.csv");

        reading_csv.print_csv(matrix);
    }
}