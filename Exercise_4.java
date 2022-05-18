/*
 * Time Complexity: O(nLogn), always divides the array into two 
 * halves and takes linear time to merge two halves.
 * 
 * Space Complexity: O(n), where n is the size of array
 */
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    	/**
         * We get sizes of two halved arrays and their respective index range.
         * We are creating subArrays based on that, provided mid value, begin and end
         * index and we add elements into them respectively.
         * Then we are sorting two sorted arrays by comparing smallest element and
         * moving respective pointer, if any array has remaining elements then we add
         * those as well.
         */
       //Your code here  
      // Find sizes of two subarrays to be merged	
    	int n1 = m - l + 1;
    	int n2 = r - m;
    	
    	int L[] = new int[n1];
    	int R[] = new int[n2];
    	
    	for(int i = 0; i < n1; ++i) {
    		L[i] = arr[l + i];
    	}
    	
    	for(int j = 0; j < n2; ++j) {
    		R[j] = arr[m + 1 + j];
    	}
    	
    	int a=0;
    	int b=0;
    	
    	int k = l;
    	while(a < n1 && b < n2) {
    		if(L[a] <= R[b]) {
    			arr[k] = L[a++];
    		} else {
    			arr[k] = R[b++];
    		}
    		k++;
    	}
    	
    	while (a < n1) {
            arr[k++] = L[a++];
        }
    	
    	while (b < n2) {
            arr[k++] =R[b++];
        }
   	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    	//Write your code here
    	//Call mergeSort from here 
    	/**
         * Here we are checking if beginning index is smaller than end index, then get
         * mid so that we can sort 2 divided arrays recursively.
         * and then we call the merge function, to merge them once they are sorted.     
         */
    	
    	if(l < r) {
    		int mid = (l + r) / 2;
    		
    		sort(arr, l, mid);
    		sort (arr, mid + 1, r);
    		
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
