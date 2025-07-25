/** space complexity: O(n)
* time complexity: O(n log n)
* did this code successfully run on Leetcode: This is not a Leetcode problem
* any problem you faced while coding this: No
*/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int n1 = m - l + 1; 
       int n2 = r - m; 
    
    /**  Create temp arrays
     * Create two temporary arrays to hold the elements of the two subarrays 
     * The first subarray is from index l to m and the second subarray is from m+1 to r
     * The size of the first subarray is n1 and the size of the second subarray is n2
     */
        int L[] = new int[n1]; 
        int R[] = new int[n2]; 

    // Copy data to temp arrays 
        for (int i=0; i<n1; ++i) 
            L[i] = arr[l + i]; 
        for (int j=0; j<n2; ++j) 
            R[j] = arr[m + 1 + j]; 
  
    /** Merge the temp arrays 
    * Initial indexes of first and second subarrays 
    */
    int i = 0, j = 0;

    /** Initial index of merged subarray array 
    * The arr[k] will modify the original array with the sorted elements
    */
    int k = l; 
        while (i < n1 && j < n2) { 
            if (L[i] <= R[j]) { 
                arr[k] = L[i]; 
                i++; 
            } else { 
                arr[k] = R[j]; 
                j++; 
            } 
            k++; 
        } 
  
    // Copy remaining elements of L[] if any 
        while (i < n1) { 
            arr[k] = L[i]; 
            i++; 
            k++; 
        } 

    // Copy remaining elements of R[] if any 
        while (j < n2) { 
            arr[k] = R[j]; 
            j++; 
            k++; 
        }
    } 
  
     // Main function that sorts arr[l..r] using 
    // merge() 
    // Divide each subarray until no more elements can be divided into two halves and sort them recursively
    // All recursive calls are listed in the call stack until the base case is reached 
    // Then the merge function is called to combine the sorted subarrays
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    //Call mergeSort from here 
    if (l < r) { 
            int m = (l + r) / 2; 
  
            // Sort first and second halves 
            sort(arr, l, m); 
            sort(arr, m + 1, r); 
  
            // Merge the sorted halves 
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