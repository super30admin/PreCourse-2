// Time Complexity : O(nlogn)
// Space Complexity : O(n) space needed while merging
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : yes, few problems, regarding the algorithm but I found the detailed explanation in youtube, so I was able to code it out at last.


// Your code here along with comments explaining your approach
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int n1 = m-l+1;
       int n2 = r-m;
        // two arrays initialized to left and right subarray sizes
       int[] left = new int[n1];
       int[] right = new int[n2];

       //copied the elements from original array to subarrays.
       for(int i=0; i<n1; i++)
        left[i] = arr[l+i];
        for(int i=0; i<n2; i++)
        right[i] = arr[m+1+i];


       int i =0;
       int j = 0;
       int index = l;
       //now, which ever element is smaller from left anf right will be copied to original array repeatedly, there by the array becomes sorted.
       while(i<n1 && j<n2)
       {
            if(left[i] <=right[j])
            {
               arr[index] = left[i];
                index++;
                i++;
            }
            else
            {
                arr[index] = right[j];
                index++;
                j++;
            }
       }
       //if there are any extra elements left in left subarray
       while(i<n1)
       {
            arr[index] = left[i];
            i++;
            index++;
       }
        //if there are any extra elements left in right subarray
       while(j<n2)
       {
            arr[index] = right[j];
            j++;
            index++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        //recursively called the sort method to partition the array into two parts.
        //at last called the merge to merge the subarrays.
        if(l<r)
        {
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
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