// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int l1 = l;
       int l2 = m+1;
       int tot = -l+1+r;
       int add = 0;
       int[] dup = new int[tot];
       while(l2 <=r && l1<=m)
       {
            if(arr[l1]<=arr[l2])
            {
                //System.out.println(arr[l1]); 
                dup[add] = arr[l1];
                l1++;
                add++;
            }
            else
            {
                //System.out.println(arr[l2]); 
                dup[add] = arr[l2];
                l2++;
                add++;
            }
       }
       while(l2<=r)
       {
            dup[add] = arr[l2];
            l2++;
            add++;
       }
       while(l1<=m)
       {
            dup[add] = arr[l1];
            l1++;
            add++;
       }
       l2 = l;
       for(int i=0;i<dup.length;i++)
       {
        arr[l+i] = dup[i];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l<r)
        {
            int mid = (l+r)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
        }
        //Call mergeSort from here 
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