class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	//size of left and right arrays
    	int n1 = m-l+1;
    	int n2 = r-m;
    	
    	//initializing left and right array
    	int[] L = new int[n1];
    	int[] R = new int[n2];
    	
    	//copy elements into left and right array
    	for(int i=0; i< n1; i++)
    		L[i] = arr[l+i];
    	for(int j=0; j< n2; j++)
    		R[j] = arr[m+1+j];
    	
    	//pointers for copying 
    	int i=0, j=0, k=l;
    	//merge two temp arrays into arr
    	while(i< n1 && j< n2)
    	{
    		if(L[i] <= R[j]) 
    		{
    			arr[k] = L[i];
    			i++;   			
    		}else
    		{
    			arr[k] = R[j];
    			j++;
    		}
    		k++; 
    	}
    	while (i< n1)
    	{
    		arr[k] = L[i];
    		i++;k++;
    	}
    	while (j < n2)
    	{
    		arr[k] = R[j];
    		j++;k++;
    	}
    } 
    // Approach: sort function divides the array into two halves and 
    //merge function - we basically merge the two arrays L and R into this arr 
    //by comparing each element
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l < r)
    	{
    		int m= (l+r)/2;
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

//Time Complexity : O(n log n)
//Space Complexity : O(1) no extra space is used
//Did this code successfully run on Leetcode : NA
//Any problem you faced while coding this : No