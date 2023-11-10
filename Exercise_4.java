/*
 * Time Complexity :O(nlog(n))
 * Space Complexity : O(N) N is number of elemnts inserted into the stack.
 * Did this code successfully run on Leetcode : Didn't see this problem on Leetcode and hence solve locally.
 * Any problem you faced while coding this : NO
 * 
 */
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    	int leftMergeSize = m - l + 1;
        int rightMergeSize = r - m;

         int leftMerge[] = new int[leftMergeSize];
         int rightMerge[] = new int[rightMergeSize];

         for (int i = 0; i < leftMergeSize; i++)
         {
             leftMerge[i] = arr[l + i];
         }

         for (int j = 0; j < rightMergeSize; j++)
         {
             rightMerge[j] = arr[m + 1 + j];
         }

         int i = 0;
         int j = 0;
         int k = l;

         while(i < leftMergeSize && j < rightMergeSize)
         {
             if (leftMerge[i] <= rightMerge[j])
             {
                 arr[k] = leftMerge[i];
                 i++;
             }
             else
             {
                 arr[k] = rightMerge[j];
                 j++;
             }
             k++;
         }

         while (i < leftMergeSize)
         {
             arr[k] = leftMerge[i];
             i++;
             k++;
         }

         while (j < rightMergeSize)
         {
             arr[k] = rightMerge[j];
             j++;
             k++;
         }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    	//Write your code here
       
    	if (l < r)
        {
            int m = l + (r - l)/ 2;

            sort(arr, l, m);
            sort(arr, m + 1, r);

            //Call mergeSort from here 
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
