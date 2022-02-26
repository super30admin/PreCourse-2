// Time Complexity : O(N * Log N)
// Space Complexity : O(N) // creating 2 arrays before merging 2 sub - arrays

// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/*

Wee will divide the array till more than elements remains in sub array 
Then we will call merge() function to merge 2 sorted arrays to merge to make sorted nresultant array

*/



class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int len1 = m - l + 1; // Left subarray
       int len2 = r - m; // Right subarray


       int left[] = new int[len1];
       int right[] = new int[len2];

       for(int c = 0; c< len1; c++){
           left[c] = arr[l + c]; 
       }
       for(int c = 0; c< len2; c++){
           right[c] = arr[m + 1 + c];
       }

       int i = 0, j = 0 , k = l;

       while(i < len1 && j < len2){
           if(left[i] <= right[j]){
                arr[k] = left[i];
                i++;
           }
           else{
               arr[k] = right[j];
               j++;
           }
           k++;
       }

       while(i < len1){
           arr[k++] = left[i++];
       }
       while(j < len2){
           arr[k++] = right[j++];
       }



    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l < r)
        {
            int mid =  l +  (r - l)  / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
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