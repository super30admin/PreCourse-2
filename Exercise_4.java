// Time Complexity : Still working;
// Space Complexity : Using new array for copy, so "O(N) + Stack Function O(Log(N))"
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Calculating  complexities
import java.util.Arrays;

class MergeSort {
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
        //Your code here
        System.out.println("Merge : l,mid,r : " + l + "," + m + "," + r);
        int arr1_ctr = 0;
        int arr2_ctr = 0;
        int[] arr1 = Arrays.copyOfRange(arr, l, m + 1);
        int[] arr2 = Arrays.copyOfRange(arr, m + 1, r + 1);
        // Checking array splits
        System.out.print("Split : Arr1 [");
        for (int i : arr1
        ) {
            System.out.print(i + ",");
        }
        System.out.print("]; Arr2 [");
        for (int i : arr2
        ) {
            System.out.print(i + ",");
        }
        System.out.println("]");
        // Comparing elements in two arrays and adding to main arr
        int main_arr = l;
        while (arr1_ctr < arr1.length && arr2_ctr < arr2.length) {
            //System.out.println("Checking arr1_ctr : " + arr1_ctr + ", arr2_ctr : " + arr2_ctr);
            if (arr1[arr1_ctr] < arr2[arr2_ctr]) {
                arr[main_arr] = arr1[arr1_ctr];
                arr1_ctr = arr1_ctr + 1;
            } else {
                arr[main_arr] = arr2[arr2_ctr];
                arr2_ctr = arr2_ctr + 1;
            }
            main_arr++;
        }
        //System.out.print("Rem elem 1 : "+arr1_ctr+" /len "+arr1.length);
        while (arr1_ctr < arr1.length) {
            arr[main_arr] = arr1[arr1_ctr];
            arr1_ctr++;
            main_arr++;
        }
        System.out.println();
        while (arr2_ctr < arr2.length) {
            //System.out.println("Rem elem 2 :"+arr1_ctr+" /len "+arr2.length);
            arr[main_arr] = arr2[arr2_ctr];
            arr2_ctr++;
            main_arr++;
        }
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) {
        //Write your code here
        //Call mergeSort from here
        int mid = (l + r) / 2;
        System.out.println("Sort l,mid,r : " + l + "," + mid + "," + r);
        if (l < r) {
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
            printArray(arr);
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
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 