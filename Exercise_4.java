//Time Complexity :O(n.log n)
//Space Complexity :O(n.log n)
//Did this code successfully run on Leetcode : N/a
//Any problem you faced while coding this : N/A

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
		// Your code here
		int n1 = m - l + 1; // length of 2 sub arrays
		int n2 = r - m;
		
		int lr[] = new int[n1]; // forming temp left Array
		int rr[] = new int[n2]; // Right array
		
		for(int i=0; i<n1 ;++i) 
			lr[i]=arr[l + i];   // copying to temp arrays lr, rr;
		for(int j=0; j<n2 ;++j) 
			rr[j]=arr[m + 1 + j];
		
		
		// Merging them here
		int i=0,j=0,k=l; // initialization before to merge 2 sorted arrays
		
		while(i<n1 && j<n2) {
			if(lr[i] <= rr[j]) {
				arr[k] = lr[i];
				i++;
			}
			else {
				arr[k] = rr[j];
				j++;
			}
			k++;
		}
		
		// remaining elements just move them in the back
		while(i<n1) {
			arr[k] = lr[i];
			i++;
			k++;
		}
		while(j<n2) { // Similarly in right array
			arr[k] = rr[j];
			j++;
			k++;
		}
		
		
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) { // recursive Approach
		// Write your code here
		// Call mergeSort from here
		
		if(l<r) {
			int mid = l + (r-l)/2;
			
			sort(arr,l,mid); // top Down Approach breaking in half
			sort(arr,mid+1,r); // left array & right array sorting
			
			merge(arr,l,mid,r); // Finally merging the sorted array, 
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
