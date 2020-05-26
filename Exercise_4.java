// Time Complexity : o(nlog n)
// Space Complexity : o(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
	    	//Your code here  
	    	int n1 = m - l + 1;
	    	int n2 = r - m;
	
	    	int[] a1 = new int[n1];
	    	int[] a2 = new int[n2];
	
	    	for (int i = 0; i < n1; i++) {
	    		a1[i] = arr[l + i];
	    	}
	
	    	for (int i = 0; i < n2; i++) {
	    		a2[i] = arr[m + 1 + i];
	    	}
	    	
	    	int i = 0, j = 0, k = l;
	   
	    	while (i < n1 && j < n2) {
	    		if(a1[i] <= a2[j]) {
	    			arr[k] = a1[i];
	    			i++ ;
	    		}else {
	    			arr[k] = a2[j];
	    			j++;
	    		}
	    		k++;
	    	}
	    	
	    	while(i < n1) {
	    		arr[k] = a1[i];
	    		k++; i++;
	    	}
	    	
	    	while(j < n2) {
	    		arr[k] = a2[j];
	    		k++; j++;
	    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
    		if(l < r) {
    			int mid = (l + r)/2;
    			sort(arr,l,mid);
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