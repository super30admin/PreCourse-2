// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //indexes for temp arrays
       int n1 = m - l +1;
       int n2 = r - m;
       
       //initialize temp arrays
       int left[] = new int[n1];
       int right[] = new int[n2];

       //add elements to temp arrays
       for (int i=0; i<n1; i++) {
           left[i] = arr[l+i];
       }
       for (int j=0; j<n2; j++) {
           right[j] = arr[m+1+j];
       }

       int i=0, j=0;

       //maintain new low for merging the two temp arrays
       int k = l;

       //compare and merge the 2 temp arrays
       while(i<n1 && j<n2) {
           if(left[i] <= right[j]) {
               arr[k++] = left[i++];
           } else {
               arr[k++] = right[j++];
           }
       }
       while (i<n1) { //add remaining items from left array
           arr[k++] = left[i++];
       }
       while(j<n2) { //add remaining items from right array
           arr[k++] = right[j++];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Call mergeSort from here 
        if (l<r) {
            int mid = l + (r-l)/2; //calculate mid

            sort(arr,l,mid); //sort the 1st half of array
            sort(arr, mid+1, r);//sort the 2nd half

            merge(arr, l, mid, r); //merge the sorted halves
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