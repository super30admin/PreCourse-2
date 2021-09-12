class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int leftArr[] = new int [m-l+1];
    	int rightArr[] = new int [r-m];
    	for(int i = l, j=0; i<=m; i++, j++) {
    		leftArr[j] = arr[i];
    	}
    	for(int i = m+1, j=0; i<=r; i++, j++) {
    		rightArr[j] = arr[i];
    	}
    	int i =0, j=0, k = l;
    	while(i<leftArr.length && j<rightArr.length) {
    		arr[k++] = leftArr[i] <= rightArr[j] ? leftArr[i++] : rightArr[j++];
    	}
    	while(i<leftArr.length) {
    		arr[k++] = leftArr[i++];
    	}
    	while(j<rightArr.length) {
    		arr[k++] = rightArr[j++];
    	}
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l>=r) {
    		return;
    	}
    	int mid = l+ (r-l)/2;
    	sort(arr,l,mid);
    	sort(arr,mid+1,r);
    	merge(arr,l,mid,r);
    	
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