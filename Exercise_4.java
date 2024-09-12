class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int[] temp = new int[arr.length];
    	for(int i=0;i<arr.length;i++) {
    		temp[i] = arr[i];
    	}
    	int i = l, j = m+1, k = l;
    	while(i<=m && j<=r) {
    		if(temp[i] <= temp[j]) {
    			arr[k++] = temp[i++];
    		}else {
    			arr[k++] = temp[j++];
    		}
    	}
    	
    	for(; i<=m;i++) {
    		arr[k++] = temp[i];
    	}
    	for(; j<=r;j++) {
    		arr[k++] = temp[j];
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l < r) {
    		int mid = l +(r-l)/2;
        	sort(arr, l, mid);
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

//Time Complexity : O(nlog(n))
//Space Complexity : O(n) 
//Did this code successfully run on Leetcode :
//Any problem you faced while coding this : No