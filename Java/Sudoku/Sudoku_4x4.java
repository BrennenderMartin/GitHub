package Sudoku;

import java.util.Scanner;

public class Sudoku_4x4 {

    public static void main(String[] args) {
        new Sudoku_4x4();
    }

    int x;
    int y;
    int value;

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
    Scanner scanner = new Scanner(System.in);

    public Sudoku_4x4() {
        while (solved == false) {
            print_matrix();
            ask();
            check_right_num();
            check_if_finished();
        }
        System.out.println("Congratiulations, you hava solved this Sudoku! :)");
    }
    
    private void print_matrix() {
        for (int y = 0; y < matrix.length; y++) {
            String text = "";
            for (int x = 0; x < matrix[y].length; x++) {
                text += matrix[y][x] + " ";
            }
            System.out.println(text);
        }
        System.out.println();
    }

    private void ask() {
        System.out.println("Please enter a row, which you want to change");
        y = scanner.nextInt() - 1;

        System.out.println("Please enter a column, which you want to change");
        x = scanner.nextInt() - 1;

        System.out.println("Please enter the value you want it to change to");
        value = scanner.nextInt();
        
        System.out.println();
    }

    private void check_right_num() {
        if(value == matrix_solved[y][x]) {
            matrix[y][x] = value;
        } else {
            System.out.println("[read with asian accent] Wong Numbah Madafacka!!!");
            System.out.println();
        }
    }

    private void check_if_finished() {
        int trueCount = 0;
        for (int y = 0; y < matrix.length; y++) {
            for (int x = 0; x < matrix[y].length; x++) {
                if (matrix[y][x] == matrix_solved[y][x]) {
                    trueCount++;
                }
            }
        }
        if (trueCount == 16) {
            solved = true;
        }
    }
}