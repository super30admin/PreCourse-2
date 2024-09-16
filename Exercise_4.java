class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int[] left = new int[m-l+1];
    	int[] right = new int[r-m];
    	
    	for(int i = 0; i < m-l+1; i++) {
    		left[i] = arr[i+l];
    	}
    	for(int i = 0; i < r-m; i++) {
    		right[i] = arr[m+1+i];
    	}
    	
    	int i = 0, j = 0, k = l;
    	while(i < m-l+1 && j < r-m) {
    		if(left[i] < right[j]) {
    			arr[k] = left[i++];
    		}
    		else {
    			arr[k] = right[j++];
    		}
    		k++;
    	}
    	while(i < m-l+1) {
    		arr[k++] = left[i++];
    	}
    	while(j < r-m) {
    		arr[k++] = right[j++];
    	}
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l < r) {
    		int m = (l+r)/2;
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
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 