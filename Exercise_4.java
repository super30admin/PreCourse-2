/*******
Exercise_4 : Merge Sort.

Time Complexity :                               O(n Logn)
Space Complexity :                              O(n)  
Did this code successfully run on Leetcode :    No (Could not find on leetcode)
Any problem you faced while coding this :       Difficult to implement and understand how to calculate time and space complexity
*******/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[left..mid] 
    // Second subarray is arr[mid+1..right] 
    void merge(int arr[], int left, int mid, int right) 
    {  
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0;
        int k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[left..right] using merge() 
    void sort(int arr[], int left, int right) 
    { 
	    if ( left < right ){
            int mid = ( left + right ) /2;
            sort(arr, left, mid);
            sort(arr, mid + 1, right);

            merge(arr, left, mid, right);
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