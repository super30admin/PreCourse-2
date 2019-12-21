class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int length1 = m-l+1;
    	int length2 = r - m;
    	
    	int leftList[] = new int[length1];
    	int rightList[] = new int[length2];
    	
    	for(int i=0; i<length1; i++) {
    		leftList[i] = arr[i+l];
    	}
    	
    	for(int i=0; i<length2; i++) {
    		rightList[i] = arr[i+m+1];
    	}
    	
    	int i=0, j=0;
    	int lowIndex = l;
    	while(i < length1 && j < length2) {
    		if(leftList[i] <= rightList[j]) {
    			arr[lowIndex] = leftList[i];
    			i++;
    		}else {
    			arr[lowIndex] = rightList[j];
    			j++;
    		}
    		
    		lowIndex++;
    	}
    	
    	while(i < length1) {
    		arr[lowIndex] = leftList[i];
    		i++;
    		lowIndex++;
    	}
    	
    	while(j < length2) {
    		arr[lowIndex] = rightList[j];
    		j++;
    		lowIndex++;
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