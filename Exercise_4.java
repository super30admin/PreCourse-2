/**
 * Implemented the sort in ascending order
 * 
 * space complexity is O(n) as no additional space is allocated and the array is sorted inplace.
 * 
 * time complexity is O(nlog(n)) as the array is split in half recursively, which would result in logn recursive calls and at each
 * recursive call it takes o(n) to merge.. so effectively it is O(nlogn)
 * 
 * took a while to think through the recursion.
 */

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int i = l;
       int j = l;
       int k = m+1;
       while (i <= r && k <=r ) {
           if(arr[j] <= arr[k]) {
               j++;
           }
           else 
           {
                int temp = arr[j];
                arr[j] = arr[k];
                arr[k] = temp;
                k++;
           }
           i++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(r-l > 1)
        {
            sort(arr, l, (l+r)/2);
            sort(arr, (l+r)/2 +1, r);
            merge(arr, l, (l+r)/2, r);
        }
        else
        {
            if(arr[l] > arr[r]) 
            {
                int temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;
            }

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