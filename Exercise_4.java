// Time Complexity :O(n logn)
// Space Complexity : O(n) n-length of the array.
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : merge function is confusing
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
	    int l1=m-l+1; //defining length for the two arrays
	    int l2=r-m;	   
	    int[] first=new int[l1];// Allocating memory to two arrays
	    int[] second=new int[l2];
	    for(int i=0;i<l1;i++)
			first[i]=arr[i+l]; //assigning left to middle values to first array
		for(int i=0;i<l2;i++)
			second[i]=arr[i+m+1]; // assigning right to middle values in the second array.
		int i=0,j=0,k=l;
		while(i<l1 && j<l2) // When both arrays are not null
		{
			if(first[i]<=second[j]) // If first array contains a lesser element
			{
				arr[k]=first[i]; // Assign the value from first array to arr
				i++;
			}else{ // If second array contains a lesser element than first array
				arr[k]=second[j]; // Assign the value from second array to arr
				j++;
			}
			k++;
		}
		while(i<l1) // If second array is null then allocate all the remaining values from first array to arr
		{
			arr[k]=first[i];
			k++;
			i++;
		}
		while(j<l2)// If first array is null then allocate all the remaining values from second array to arr
		{
			arr[k]=second[j];
			j++;
			k++;
		}
			
			
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
		if(l<r)
		{
		//Call mergeSort from here 
		int mid=l+(r-l)/2;
		sort(arr,l,mid-1);
		sort(arr,mid+1,r);
		merge(arr,l,mid,r);
		
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