class MergeSort 
{ 
	
    /**
     * Time Complexity: O(nlog(n))
     * Space Complexity: O(n)
     * Author: Rahul Udhayakumar
     */
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    	 int leftArrSize = m - l + 1;
         int rightArrSize = r - m;

         // Initialize two new arrays
         int[] leftArr = new int[leftArrSize];
         int[] rightArr = new int[rightArrSize];

         // Populate both arrays with left and right values
         for (int i=0; i<leftArrSize; i++) {
             leftArr[i] = arr[l + i];
         }

         for (int j=0; j<rightArrSize; j++) {
             rightArr[j] = arr[m + 1 + j];
         }


         // Sort the main array with two pointers
         int y = 0, z = 0;

         for (int k=l; k<=r; k++) {
             if (z >= rightArrSize || (y < leftArrSize && leftArr[y] <= rightArr[z])) {
                 arr[k] = leftArr[y];
                 y++;
             } else {
                 arr[k] = rightArr[z];
                 z++;
             }
         }  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if (l < r) {
            int middle = (int) Math.floor((l+r)/2);
            sort(arr, l, middle);
            sort(arr, middle+1, r);
            merge(arr, l, middle, r);
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