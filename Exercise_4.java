// Time Complexity : O(nlog(n))
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int size_arrat1 = m - l + 1;
       int size_arrat2 = r - m;

       int left_part[] = new int[size_arrat1];
       int right_part[] = new int[size_arrat2];

       for (int i = 0; i < size_arrat1; ++i)
       left_part[i] = arr[l + i];
       for (int j = 0; j < size_arrat2; ++j)
       right_part[j] = arr[m + 1 + j];

       int i = 0, j = 0;
       int k = l;
       while (i < size_arrat1 && j < size_arrat2) {
           if (left_part[i] <= right_part[j]) {
               arr[k] = left_part[i];
               i++;
           }
           else {
               arr[k] = right_part[j];
               j++;
           }
           k++;
       }

       while (i < size_arrat1) {
           arr[k] = left_part[i];
           i++;
           k++;
       }

       while (j < size_arrat2) {
           arr[k] = right_part[j];
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
        if (l < r) {
            int middle =l+ (r-l)/2;
            sort(arr, l, middle);
            sort(arr, middle + 1, r);
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