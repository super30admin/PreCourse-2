class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int l1 = m-l+1;
    	int l2 = r-m;
    	int[] arr1 = new int[l1];
    	int[] arr2 = new int[l2];
    	for(int i=0; i<l1; i++) {
    		arr1[i] = arr[l+i];
    	}
    	for(int i=0; i<l2; i++) {
    		arr2[i] = arr[i+m+1];
    	}
    	int i = 0, j = 0;
    	int temp = l;
    	// merging the 2 temp arrays to the main array
    	while(i < l1 && j < l2) {
    		if (arr1[i] <= arr2[j]) { 
                arr[temp] = arr1[i]; 
                i++; 
            } 
            else { 
                arr[temp] = arr2[j]; 
                j++; 
            } 
            temp++;
    	}
    	
    	//this gets executed if there are still any elements left for merging this case arises when the 2 temp arrays are of variable length
    	while(i<l1) {
    		arr[temp] = arr1[i];
    		i++;
    		temp++;
    	}
    	while(j<l2) {
    		arr[temp] = arr2[j];
    		j++;
    		temp++;
    	}
    } 
    
    void sort(int arr[], int l, int r) 
    {
    	//dividing the arrays and then calling the merge function
    	if(l < r) {
	    	int mid = (l+r)/2;
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