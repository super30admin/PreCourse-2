
/*
 * * Time Complexity: O(n log n)
 * 
 * Space Complexity: O(1)
 * 
 * This code can run successfully on Leetcode
 * 
 * Any problems you face while coding this - No
 * 
 * Approach: 
 * 1. In this, we calculate mid point of array. Based on this mid point we divide array into two halfes
 * 	  first from start to mid and second from mid+1 to end
 * 2. We sort this two array and then merge them together recursively to form final sorted array
 *
 */
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int first = m - l + 1;
    	int sec = r - m;
    	
    	int[] temp_f = new int[first];
    	int[] temp_s = new int[sec];
    	
    	for(int i = 0; i < first;i++) {
    		temp_f[i] = arr[l + i];
    	}
    	
    	for(int i = 0; i < sec;i++) {
    		temp_s[i] = arr[m + 1 + i];
    	}
    	
    	int i = 0; int j = 0; int k = l;
    	
    	while(i < first && j < sec) {
    		if(temp_f[i] <= temp_s[j]) {
    			arr[k] = temp_f[i];
    			i++;
    		}else {
    			arr[k] = temp_s[j];
    			j++;
    		}
    		k++;
    	}
    	
    	while(i < first) {
    		arr[k] = temp_f[i];
    		i++;
    		k++;
    	}
    	
    	while(j < sec) {
    		arr[k] = temp_s[j];
    		j++;
    		k++;
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	
    	if(l < r) {
    		int mid = l + (r - l) / 2;
    		
    		sort(arr, l, mid);
    		sort(arr, mid+1 , r);
    		
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