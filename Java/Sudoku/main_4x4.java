package Java.Sudoku;

import java.util.Scanner;

public class main_4x4 {

    public static void main(String[] args) {
        new main_4x4();
    }

    int[][] matrix = {
        {0, 0, 0, 3},
        {0, 4, 0, 0},
        {1, 0, 0, 4},
        {0, 0, 3, 0}
    };
    int[][] matrix_solved = {
        {2, 1, 4, 3},
        {3, 4, 1, 2},
        {1, 3, 2, 4},
        {4, 2, 3, 1}
    };
    boolean solved = false;

    main_4x4() {
        print_matrix();
        
        int x;
        int y;
        int value;
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Please enter a row, which you want to change");
            y = scanner.nextInt() - 1;

            System.out.println("Please enter a column, which you want to change");
            x = scanner.nextInt() - 1;

            System.out.println("Please enter the value you want it to change to");
            value = scanner.nextInt();
        }
        System.out.println(matrix_solved[y][x]);
        if(value == matrix_solved[y][x]) {
            matrix[y][x] = value;
        } else {
            System.out.println("[read with asian accent] Wong Numbah Madafacka!!!");
        }
        
    }
    
    private void print_matrix() {
        for (int y = 0; y < matrix.length; y++) {
            String text = "";
            for (int x = 0; x < matrix[y].length; x++) {
                text += matrix[y][x] + " ";
            }
            System.out.println(text);
        }
    }
}