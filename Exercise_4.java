class MergeSort 
{ 
    //O(N) space compared to O(1) space for quick sort
    
    /*
    Note:
    Quick sort is typically faster than merge sort when the data is stored in memory. However, when the data set is huge and is stored on external devices such as a hard drive, merge sort is the clear winner in terms of speed. It minimizes the expensive reads of the external drive and also lends itself well to parallel computing.
    */
    // O(N log N) average and worst case complexity
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int left, int mid, int right) 
    {  
       //O(N) extra space to merge subarrays
       int[] larr = new int[mid+1-left];
       int[] rarr = new int[right-mid];

       //Load subarrays with values   
       for(int i = 0; i < larr.length; i++)
            larr[i] = arr[left+i];

       for(int i = 0; i < rarr.length; i++)
            rarr[i] = arr[mid+1+i];

        //i = least index of larr, j = least index of rarr, k = least index of arr
        int i = 0, j = 0, k = left;
        while(i < larr.length && j < rarr.length) {
              //Compare values at current indices in larr and rarr
              if(larr[i] <= rarr[j]) {
                  arr[k++] = larr[i++];
              }
              else
                  arr[k++] = rarr[j++];
        }
        //Copy remaining elements if larr and rarr lengths are unequal
        while(i < larr.length) arr[k++] = larr[i++];
        while(j < rarr.length) arr[k++] = rarr[j++];

    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int left, int right) 
    { 
        //Call sort and merge on subarrays until left equals right
        if(left < right) {
            int mid = (left+right)/2;
            sort(arr,left,mid);
            sort(arr,mid+1,right);
            merge(arr,left,mid,right);
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