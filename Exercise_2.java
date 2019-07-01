class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here   
        if(i<arr.length && j<arr.length) { // Checking the i and j around the max value that can fit in arr.
		int ival = arr[i];
		int jval = arr[j];
		arr[i] = jval;
		arr[j] = ival;
    	}
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
        int pivot = high; //intially we take the pivot the nth value in array.
    	int small = low;

    	for (int i=small; i<high; i++) {
    		 if(arr[i]<arr[high]) {
    			 swap(arr,i,small);   //swapping i value with small value in the array.
    			 small++;		     //increment small pointer value.
    		 }
    	 }
    	 swap(arr,small,pivot);    //after traversing n element, swap the small and pivot , to get the pivots exact location in the array.
    	 return small; 		       //return the small value. ( here we are returning the small value, because it is the 
                                   //actual pivot value in the array i.e. where pivot needs to be in array.
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
           
        //Base Case
    	if(low<high) { // this is the case where sort methods needs to be stop.
	    	int p  = partition(arr,low,high);  //get the ordered position  of the element at high.
	    	sort(arr,low,p-1); //sorting the left hand side of p
	    	sort(arr,p+1,high);  //sorting the right hand side of p
    	}
            
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
