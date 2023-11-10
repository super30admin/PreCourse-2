// Time Complexity : O(nlogn)
// Space Complexity :O(n)
// Any problem you faced while coding this : Was unable to implement, had to take a lot of help from internet

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       // get length for two arrays
       int length1 = m - l + 1;
       int length2 = r - m;
 
       // create left and right array
       int left[] = new int[length1];
       int right[] = new int[length2];
 
       // Insert data into left and right array from l to mid and mid+1 to h
       for (int i = 0; i < length1; i++)
           left[i] = arr[l+i];
       for (int j = 0; j < length2; j++)
            right[j] = arr[m+1+j];
 
       
 
       // create pointers to iterate through left and right array
       int i = 0, j = 0;
 
       // k will serve as pointer for input arr
       int k = l;
       // iterate through left and right array
       while (i < length1 && j < length2) {
        /*Compare the left and right element
        * If left's element is less or equal to right  place it at k position in arr
        *then increment the pointer i
        *otherwise place the element from right array at k position as it is smaller 
        *Then increment as k position is sorted
        *
        */ 
           if (left[i] <= right[j]) {
               arr[k] = left[i];
               i++;
           }
           else {
               arr[k] = right[j];
               j++;
           }
           k++;
       }
 
       // If any elements are remaining in the left array copy it at the end of arr 
       while (i < length1) {
           arr[k] = left[i];
           i++;
           k++;
       }
 
       // If any elements are remaining in the right array copy it at the end of arr /
       while (j < length2) {
           arr[k] = right[j];
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
        // If l is less than r then only call merge sort
        // Otherwise the array is sorted, as only one element is present
        if (l < r) {
            // Calculate mid
            int mid =l+ (r-l)/2;
  
            // Sort sort left and right
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
  
            // Merge the sorted arrays
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