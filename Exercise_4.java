class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //find the size of two sub arrays
        int s1 = m-l+1;
        int s2 = r-m;
        int larr[] = new int[s1];
        int rarr[] = new int[s2];
        /*Copy data to temp arrays*/
        for (int i = 0; i < s1; ++i)
            larr[i] = arr[l + i];
        for (int j = 0; j < s2; ++j)
            rarr[j] = arr[m + 1 + j];

        /* Merge the temp arrays */

        // Initial indexes of first and second subarrays
        int i = 0, j = 0;

        // Initial index of merged subarray array
        int k = l;
        while (i < s1 && j < s2) {
            if (larr[i] <= rarr[j]) {
                arr[k] = larr[i];
                i++;
            }
            else {
                arr[k] = rarr[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of L[] if any */
        while (i < s1) {
            arr[k] = larr[i];
            i++;
            k++;
        }

        /* Copy remaining elements of R[] if any */
        while (j < s2) {
            arr[k] = rarr[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l<r){
            // find mid point
            int m = l+(r-l)/2;
            // Sort first half an second half
            sort(arr, l,m);
            sort(arr,m+1, r);
            //Call mergeSort from here
            merge(arr,l,m,r);
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