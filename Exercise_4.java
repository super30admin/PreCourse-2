//Time Complexity: Average case: O(nlogn) 
//Space Complexity: O(n)
//Did the code successfully run on Leetcode: Yes
//Any problem faced while coding this: No
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       // sizes of the two halves
        int n1 = m - l + 1;
        int n2 = r - m;

        // create temp arrays
        int[] L = new int[n1];
        int[] R = new int[n2];

        // copy data into temps
        for (int i = 0; i < n1; ++i) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j];
        }

        // pointers for L[], R[], and merged array
        int i = 0, j = 0, k = l;
        // merge back into arr[l..r]
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        // copy any remaining elements of L[]
        while (i < n1) {
            arr[k++] = L[i++];
        }
        // copy any remaining elements of R[]
        while (j < n2) {
            arr[k++] = R[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if (l < r) {
            // find the midpoint to split the array
            int m = l + (r - l) / 2;

            // sort first half
            sort(arr, l, m);

            // sort second half
            sort(arr, m + 1, r);

            // merge the sorted halves
            merge(arr, l, m, r);
        }
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