// Time Complexity : The recursive solution presented performs partitioning of array in 2 parts every time till single element is remaining.
// this is a log(n) operation and merging requires traversing each partition to combine and merge taken n times.
// Hence complexity is nlog(n) for best, average and worst all cases.
// Space Complexity : Additional left and right temporary arrays are required of lengths summing up to length of array. Therefore, O(n).
// Did this code successfully run on Leetcode : Seems like Leetcode 912, solved
// Any problem you faced while coding this : Was facing incorrect answer because of assigning Right array value of arr[j+m] rather than 1 place ahead.

// Your code here along with comments explaining your approach
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        // using the middle point we have defined 2 temp arrays for Left and Right initially having single values and combines into larger array
        int[] L = new int[m-l+1];
        int[] R = new int[r-m];
       
        // assigning array values to left partition
        for(int i=0; i< L.length; i++) {
            L[i] = arr[l+i];
        }

        // assigning array values to right partition
        for(int j=0; j<R.length; j++) {
            R[j] = arr[j+m+1];
        }

        // created variables to be starting indexes to arr, Left and right arrays
        int k=l;
        int i=0;
        int j=0;

        // while left partition does not reach its end and right partition does not reach end
        while(i< m-l+1 && j<r-m) {
            // compare if left element is lesser or right and assign value to kth index or arr increment index of left with index of arr
            if(L[i]<=R[j]) {
                arr[k] = L[i];
                k++;
                i++;
            } else {
                // perform same and increment arr index and right index
                arr[k] = R[j];
                k++;
                j++;
            }
        }

        // if left partition is left with additional unmerged elements add them to end of arr
        while(i<m-l+1) {
            arr[k]=L[i];
            k++;
            i++;
        }
        // if right partition is left with additional unmerged elements add them to end of arr
        while(j<r-m) {
            arr[k] = R[j];
            k++;
            j++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 

    // Approach is to divide and conquer by splitting the array into 2 parts left and right using a mid pointer
    void sort(int arr[], int l, int r) 
    { 
    //Write your code here
        //Call mergeSort from here 
        if(l<r) {
            int mid = l+ (r-l)/2;
            
            // Performing recursive division using end as mid keeps dividing Left array into half
            sort(arr, l, mid);

            // Performing recursive division using start as mid+1 keeps dividing Right array into half
            sort(arr, mid+1, r);

            // Merge is performed which combines all divided sub arrays into sorted array
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