//Time Complexity : O(nlogn)
//Space Complexity : O(n) 
//Did this code successfully run on Leetcode : Yes 
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    	int[] arr1 = new int[m-l+1+1];
    	int[] arr2 = new int[r-m+1];
    	
    	arr1[m-l+1] = Integer.MAX_VALUE;
    	arr2[r-m] = Integer.MAX_VALUE;
    	
    	for(int h=0;h<m-l+1;h++)
    	{
    		arr1[h] = arr[l+h];
    		
    	}
    	for(int h=0;h<r-m;h++)
    	{
    		arr2[h] = arr[m+1+h];
    		
    	}
    	
    	int i=0;
    	int j=0;
    	for(int k=l;k<=r;k++)
    	{
    		
    		
    		if(arr1[i]<=arr2[j])
    		{
    			arr[k] = arr1[i];
    			i++;
    		}else
    		{
    			arr[k] = arr2[j];
    			j++;
    		}
    	}
    	 
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
    	
    	if(l<r)
    	{
    		int mid = (l+r)/2;
    		sort(arr,l,mid);
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