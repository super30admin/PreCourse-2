class MergeSort 
{ 
    // Time Complexity - O(nlogn)
    // Space Complexity - O(n)
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int i=l, j=m+1, re=0;
       int res[] = new int[r-l+1];

       while (i<=m && j<=r) {
           if (arr[i] < arr[j]) {
               res[re++] = arr[i];
               i++;
           } else {
               res[re++] = arr[j];
               j++;
           }
       }

       while (i<=m) {
           res[re++] = arr[i];
           i++;
       }

       while (j<=r) {
           res[re++] = arr[j];
           j++;
       }

       for (int x=0; x<res.length; x++) {
           arr[x+l] = res[x];
       }
       
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        int m = l+(r-l) / 2;
        if (l < r) {
            sort(arr, l, m);
            sort (arr, m+1, r);

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