// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Any problem you faced while coding this : No
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int a1 = m - l + 1;
       int a2 = r - m;

       // create 2 temp arrays 
       int arr1[] = new int[a1];
       int arr2[] = new int[a2];

       // copy 1st half to arr1
       for (int l1 = 0; l1 < a1; l1++) {
           arr1[l1] = arr[l + l1];
       }
       // copy 2nd half to arr2
       for (int l1 = 0; l1 < a2; l1++) {
           arr2[l1] = arr[m + 1 + l1];
       }

       int i = 0, j = 0, k = l;


       while (i < a1 && j < a2) {
           if (arr1[i] <= arr2[j]) {
               arr[k] = arr1[i];
               i++;
           } else {
               arr[k] = arr2[j];
               j++;
           }
           k++;
       }

       // add remaining elements of arr1
       while (i < a1) {
           arr[k] = arr1[i];
           i++;
           k++;
       }
       // add remaining elements of arr2
       while (j < a2) {
           arr[k] = arr2[j];
           j++;
           k++;
       }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if (l < r) {
            // Find the middle point
            int m = l + (r - l) / 2;
 
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