/*
Time Complexity: O(nLog n)
Space Complexity: O(n)
*/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int i = l, j = m + 1, k = 0;
       int size = r - l + 1;
       int a[] = new int[size];

       for (int x = l; x <= r; x++) {
           if (i > m) {
               a[k++] = arr[j++];
           } else if (j > r) {
               a[k++] = arr[i++];
           } else if (arr[i] < arr[j]) {
               a[k++] = arr[i++];
           } else {
               a[k++] = arr[j++];
           }
        }
           for (int p = 0; p < k; p++) {
               arr[l++] = a[p];
           }
        }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    if (l < r) {
        int mid = (l + r) / 2;

        //sort both array parts
        sort(arr, l, mid);
        sort(arr, mid + 1, r);
        //Call mergeSort from here 
        merge(arr, l, mid, r);
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