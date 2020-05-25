class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int m1 = m - l + 1 ;
    	int m2 = r - m;
    	int[] left = new int [m1];
    	int[] right = new int [m2];
    	for(int i = 0; i < m1; i++)
    		left[i] = arr[l + i];
    	for(int i = 0; i < m2; i++)
    		right[i] = arr[m + 1 + i];
    	
    	int i = 0, j = 0;
    	int k = l;
    	
    	while (i < m1 && j < m2) {
    		if (left[i] <= right[j])
    			arr[k++] = left[i++];
    		else
    			arr[k++] = right[j++];
    	
    	}
    	
    	while (i < m1 )
    		arr[k++] = left[i++];
    	
    	while(j < m2 )
    		arr[k++] = right[j++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l < r) {
    		int mid = l + (r - l) / 2;
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