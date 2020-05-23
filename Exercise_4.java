// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Running on eclipse
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int i=l,j=m+1; // two pointers i and j for tracking two parts of array, both initialized at starting of each lower and upper part respectively
       while(i<=m && j<=r) // while both pointers do not cross the end point of each lower and upper part of array respectively
       {
            if(arr[j]<arr[i]) // checking if value at j is smaller than that at i
            {   int temp = arr[i]; // swapping the two values as the value at j is smaller
                arr[i]= arr[j];
                arr[j]= temp;
                j++; // incrementing j as value at j has been checked and next value has to be checked
            }
            else
            {
                i++; // otherwise incrementing i as it is already smaller and at its right position
            }  

       }



    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r) // checking that left should not cross right
        {
            int mid = (l+r)/2; // finding mid value each split
            sort(arr,l,mid); // calling sort recursively for first half from l to mid i.e lower half of new split
            sort(arr,mid+1,r); // calling sort recursively for second half from mid+1 to r i.e upper half of new split
            merge(arr,l,mid,r); //  calling merge for merging arrays

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