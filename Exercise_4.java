//Time complexity : O(nlogn)
//Space Complexity: O(logn)
import java.util.ArrayList;
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
       void merge(int arr[], int l, int m, int r) {
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();

        // Fill the left and right temporary arrays
        for (int i = l; i <= m; i++) {
            left.add(arr[i]);
        }
        for (int i = m + 1; i <= r; i++) {
            right.add(arr[i]);
        }

        int i = 0, j = 0, k = l;

        // Merge the two arrays back into arr[]
        while (i < left.size() && j < right.size()) {
            if (left.get(i) <= right.get(j)) {
                arr[k++] = left.get(i++);
            } else {
                arr[k++] = right.get(j++);
            }
        }

        // Copy remaining elements of left[] if any
        while (i < left.size()) {
            arr[k++] = left.get(i++);
        }

        // Copy remaining elements of right[] if any
        while (j < right.size()) {
            arr[k++] = right.get(j++);
        }
    }


  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        if (l < r) {
            // Find the middle point
            int m = (l + r) / 2;

            // Sort first and second halves
            sort(arr, l, m);
            sort(arr, m + 1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }
        //Call mergeSort from here 
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 