// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        //  Size of the two subarrays
        int n1 = m - l + 1;
        int n2 = r - m;

        int arr1[] = new int[n1];
        int arr2[] = new int[n2];

        //  Copying data to subarrays
        for (int i = 0; i < n1; ++i) {
            arr1[i] = arr[l + i];
        }

        for (int i = 0; i < n2; ++i) {
            arr2[i] = arr[m + i + 1];
        }

        //  Inital indices of first, second and to be merged subarrays
        int i = 0, j = 0, k = l;

        while (i < n1 && j < n2) {
            if (arr1[i] <= arr2[j]) {
                arr[k] = arr1[i];
                i++;
            } else {
                arr[k] = arr2[j];
                j++;
            }
            k++;
        }

        //  Copying remaining elements of first subarray
        while (i < n1) {
            arr[k] = arr1[i];
            i++;
            k++;
        }

        //  Copying remaining elements of second subarray
        while (j < n2) {
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
            int m = (l+r)/2;

            //  Sorting first and second halves
            sort(arr, l, m);
            sort(arr, m + 1, r);

            //  Merging the two halves
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