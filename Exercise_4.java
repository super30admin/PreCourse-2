// Time Complexity : Time complexity of merge sort is o(nlog(n))
// Space Complexity : It requires extra space upto the length of the array so space complexity will be O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this :
//I was copying the whole array everytime in line 20,21 which was causing space issue. Looked up the algorithm for merge sort to realize we need only partial array
//Had to lookup how mergesort works

// Your code here along with comments explaining your approach

import java.util.Arrays;

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here

        int[] arr1 = Arrays.copyOfRange(arr, l, m + 1); // First half of array to merge
        int[] arr2 = Arrays.copyOfRange(arr, m + 1, r + 1); // Second half of array to merge
        int a = 0; // Pointer for first half
        int b = 0; // Pointer for second half

        int c = l; // Pointer for original array
        while (a < arr1.length && b < arr2.length) { // Loop should run till we reach to the end of first half or second
                                                     // half of the array to be sorted
            if (arr1[a] <= arr2[b]) { // If the element in first half is smaller, put that element in the final array
                arr[c] = arr1[a];
                c++;
                a++;
            } else {
                arr[c] = arr2[b]; // If the element in second half is smaller, put that element in the final array
                c++;
                b++;
            }
        }

        // If the first half has element remaining put hose elements in the final array
        while (a < arr1.length) {
            arr[c] = arr1[a];
            c++;
            a++;
        }

        // If second half has elements remaining, put those in the final array
        while (b < arr2.length) {
            arr[c] = arr2[b];
            c++;
            b++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here/
        // Recursively calling sort function until we reach an array of size 2 and then
        // calling merge function
        if (l < r) {
            int mid = l + (r - l) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}