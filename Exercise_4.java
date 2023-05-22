
// Time Complexity :
    //O(nlog(n)): for a given list of n elements, the list always gets split into halves until we have one element in each sub-list; thus we need to split log(n) no. of times
//merging happens in O(n) time.
// Space Complexity ://O(n): as we need extra arrays to store the sub-lists
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this :
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  

        int len1 = m-l+1;
        int len2 = r-m;

        int[] leftArray = new int[len1];
        int[] rightArray = new int[len2];

        //populate the two temp arrays
        for(int i=0; i<len1; i++)
        {
            leftArray[i] = arr[l+i];
        }

        for(int j=0; j<len2; j++)
        {
            rightArray[j] = arr[m+1+j];
        }
        //merge the two temp arrays
        int k =l, i=0, j=0;
        while(i<len1 && j<len2)
        {
            if(leftArray[i] <= rightArray[j])
            {
                arr[k++] = leftArray[i++];
            }
            else
            {
               arr[k++] = rightArray[j++];
            }
        }

        //if the subArrays are not of the equal length there will be elements left over in one of the lists that need
        //to be appended to our sortedArray
        for(; i<len1; i++)
        {
            arr[k++] = leftArray[i];
        }

        for (;j<len2; j++)
        {
            arr[k++] = rightArray[j];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        int m;
        if(l<r)
        {
            m = (l+r)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);
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