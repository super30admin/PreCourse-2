// Time Complexity :O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this : no

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int a[]=new int[r-l+1];
    	int index=0;
    	int i=l;
    	int j=m+1;
    	while(i<=m && j<=r){
    		if(arr[i]<=arr[j]) {
    			a[index++]=arr[i];
    			i++;
    		}else {
    			a[index++]=arr[j];
    			j++;
    		}
    	}

    	while(i<=m) {
    		a[index++]=arr[i];
    		i++;
    	}
    	while(j<=r) {
    		a[index++]=arr[j];
    		j++;
    	}

    	for(int k=0;k<a.length;k++) {
    		arr[l]=a[k];
    		l++;
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	 if(l < r)
        {
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
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