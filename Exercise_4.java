class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    // Time Complexity: O(n log(n))
    // Space Complexity: O(n)
    void merge(int arr[], int temp[], int l, int m, int r) 
    {  
       //Your code here 
       for (int k = l; k < r; k++) {
        temp[k] = arr[k];
       }
       int i = l, j = m;

       for (int k = l; k < r; k++) {
        if (i >= m) {
            arr[k] = temp[j++];
        } else if (j >= r) {
            arr[k] = temp[i++];
        } else if (temp[i] <= temp[j]) {
            arr[k] = temp[i++];
        } else {
            arr[k] = temp[j++];
        }
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    int[] temp = new int[arr.length];
        //Write your code here
        sort(arr, temp, l, r);
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  void sort(int arr[], int temp[], int l, int r) {
    if (l < r) {
        int m = l + (r-l)/2;
        sort(arr, temp, l, m);
        sort(arr, temp, m+1, r);
        merge(arr, temp, l, m, r);
    }
  }
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 