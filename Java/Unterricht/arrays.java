package Unterricht;

import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
        new arrays();
    }

    int[] array = new int[9];

    arrays() {
        for(int i = 0; i < 9; i++) {
            array[i] = i + 1;
            System.out.println(array[i]);
        }
        arrays1();
        arrays2();
    }

    // Declaration
    int[] arr;           // Preferred style
    int arr2[];          // Also valid

    // Initialization (with size)
    int[] arr3 = new int[5];  // Creates an array of size 5, initialized to 0s

    // Initialization (with values)
    int[] arr4 = {1, 2, 3, 4, 5};  // Array with 5 elements

    // Multidimensional Array
    int[][] matrix = new int[3][3];  // 3x3 matrix
    int[][] matrix2 = {{1, 2}, {3, 4}, {5, 6}};  // Initialized

    private void arrays1() {
        //arr[index];   // Access the element at the given index
        arr[0] = 10;  // Assign a value to an element

        int length = arr.length;  // Returns the size of the array (no parentheses)
        System.out.println(length);

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);  // Access each element
        }

        for (int num : arr) {
            System.out.println(num);  // Access each element
        }
        
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
    }

    private void arrays2() {
        // Fill an array with a specific value
        int[] arr = new int[5];
        Arrays.fill(arr, 42);  // {42, 42, 42, 42, 42}

        // Sort an array
        int[] unsorted = {5, 3, 1, 4, 2};
        Arrays.sort(unsorted);  // {1, 2, 3, 4, 5}

        // Binary Search (Array must be sorted)
        int index = Arrays.binarySearch(unsorted, 3);  // Returns index of 3
        System.out.println(index);

        // Copy an array
        int[] copy = Arrays.copyOf(arr, arr.length);

        // Compare arrays (returns true/false)
        boolean isEqual = Arrays.equals(arr, copy);
        System.out.println(isEqual);

        // Print array as a string
        System.out.println(Arrays.toString(arr));  // e.g., "[1, 2, 3, 4, 5]"

    }

}
