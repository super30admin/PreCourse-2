class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] marray = new int[r-l];
       int i = l, j = m, k = 0;
       while(i < m && j < r) {
            // if the left array has the small value then copy the left one
            if(arr[i] < arr[j]) {               
                marray[k++] = arr[i++];
             // if the right array has the smallest value then copy the right one
            } else {                            
                marray[k++] = arr[j++];
            }
       }

       // Copy all the remaining elements from left or right arrays
       while(i < m) {
           marray[k++] = arr[i++];
       }

       while(j < r) {
            marray[k++] = arr[j++];
       }

       // Copy the result into the original array
        for(int ctr = 0; ctr < marray.length; ctr++) {
            arr[l + ctr] = marray[ctr];
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(r - l == 1) {
            return;
        }

        // Dividing array into half recursively until there's only one element
        int m = l + (r - l) / 2;
        sort(arr, l, m);
        sort(arr, m, r);

        // Merging two unsorted arrays
        merge(arr, l, m, r+1);

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
