// Merge Sort

// Time Complexity : O(N * Log N), where N is the array's length, Merging takes N and Sorting takes LogN, 
// as it sorts in log time by dividing the array in two parts.
// Space Complexity : O(N), to store the new 2 sorted arrays we use to merge.
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here [1,2,3] & [1,3,4,5]
        // Divide them into 2 arrays
        // Those 2 arrays are already sorted,

        int x = m - l + 1, y = r - m;
        int[] xArr = new int[x];
        int[] yArr = new int[y];
        for (int i = 0; i < x; i++) {
            xArr[i] = arr[i];
        }
        for (int i = 0; i < y; i++) {
            yArr[i] = arr[m + i + 1];
        }

        // Use 2 pointer approach to compare each element
        // & swap inplace on main array.
        int p1 = 0, p2 = 0, k = l;
        while (p1 < x && p2 < y) {
            if(xArr[p1] < yArr[p2]){
                arr[k] = xArr[p1];
                p1++; k++;
            }else{
                arr[k] = yArr[p2];
                p2++; k++;
            }
        }
        while(p1<x){
            arr[k] = xArr[p1];
            p1++; k++;
        }
        while(p2<y){
            arr[k] = yArr[p2];
            p2++; k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (r > l) { // Ensures this check has at least 2 elements
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
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