class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){ 
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;	
    }
    
    int partition(int arr[], int low, int high) 
    { 
    	int mid = arr[high];//high as the pivot index
    	int lower_index = low-1;
    	for(int i=low; i<high; i++) {
    		//checking if the mid is smaller than current
    		if(arr[i]<mid ) {
    			lower_index++;
    			System.out.println(arr[lower_index]);
    			swap(arr, lower_index, i);
    		}
    	}
    	swap(arr, lower_index+1, high);
    	return lower_index+1;
    } 
    void sort(int arr[], int low, int high) 
    {  
    	
    	if(low < high) {
    		//Getting partitioning index
    		int index = partition(arr, low, high);
    		//sorting left sub array
    		sort(arr,low, index-1);
    		//sorting right sub array
    		sort(arr, index+1, high);
    	}
    	
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        for (int i=0; i<arr.length; ++i) 
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
