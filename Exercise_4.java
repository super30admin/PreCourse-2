class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
    	int leftArraySize = m - l + 1;
    	int rightArraySize = r - m;
    	int leftArray[] = new int [leftArraySize];
    	int rightArray[] = new int [rightArraySize];
    	
    	for (int i = 0; i<leftArraySize; i++) {
    		leftArray[i]=arr[l+i];
    	}
    	for (int j = 0; j<rightArraySize;j++) {
    		rightArray[j]=arr[m + 1 + j];
    	}
    	int leftIndex =0, rightIndex =0;
    	int mergedIndex = l;
    	
    	//check if left and right index do not go out of bound
    	while(leftIndex < leftArraySize && rightIndex < rightArraySize) {
    		// check if element in left array is greater than right array, then save right element into the merged array first
    		if(leftArray[leftIndex] > rightArray[rightIndex]) {
    			arr[mergedIndex] = rightArray[rightIndex];
    			rightIndex++;
    		}
    		else {
    			arr[mergedIndex] = leftArray[leftIndex];
    			leftIndex++;
    		}
    		mergedIndex++;
    	}
    	//check for remaining element in leftArray
    	while(leftIndex < leftArraySize) {
    		arr[mergedIndex] = leftArray[leftIndex];
    		leftIndex++;
    		mergedIndex++;
    	}
    	//check for remaining element in rightArray
    	while(rightIndex < rightArraySize) {
    		arr[mergedIndex] = rightArray[rightIndex];
    		rightIndex++;
    		mergedIndex++;
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l<r) {
    		int middle = l + (r - l)/2;
    		sort(arr,l, middle);
    		sort(arr, middle + 1, r);
    		
    		merge(arr, l, middle, r);
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