class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
    	 int leftArrLength = m - l + 1;
         int rightArrLength = r - m;

         int leftArray[] = new int[leftArrLength];
         int rightArray[] = new int[rightArrLength];

         for (int i = 0; i < leftArrLength; i++) {
        	 leftArray[i] = arr[l+i];
         }

         for (int j = 0; j < rightArrLength; j++) {
        	 rightArray[j] = arr[m+1+j];
         }

         int i = 0;
         int j = 0;
         int k = l;

         while (i < leftArrLength && j < rightArrLength) {
             if (leftArray[i] <= rightArray[j]){
                 arr[k] = leftArray[i];
                 i++;
             } 
             else {
                 arr[k] = rightArray[j];
                 j++;
             }
             k++;
         }

         while (i < leftArrLength) {
             arr[k] = leftArray[i];
             i++;
             k++;
         }

         while (j < rightArrLength) {
             arr[k] = rightArray[j];
             j++;
             k++;
         }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        
    	if(l < r) {							// if left is smaller than right
    		
    		int middle = (l + (r-l) / 2) ;	// finding the index of middle element
    		
    		sort(arr, l, middle);			// sorting left side of array till middle
    		
    		sort(arr, middle+1, r);			// sorting right side of array, i.e from middle till right
    		
    		//Call mergeSort from here 
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