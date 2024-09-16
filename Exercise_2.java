package precourse2;

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
   
    
    void partition(int arr[], int beg, int end) 
    { 
    	int i = beg;
    	int j = end;
    	int pivot = arr[end];
    	int temp ;
    	System.out.println("beg:"+beg+" end:"+end);
    	if(beg>=end)
    		return;
    	
		while(i < j) {
			while(arr[i] < pivot)
				i++;
			while(arr[j] >= pivot && j>i ) 
				j--;
			
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
		
		temp = arr[i];
		arr[i] = arr[end];
		arr[end] = temp;
		
		partition(arr,beg,i-1);
		partition(arr,i+1,end);
    	
 
    
    			
    	
   	//Write code here for Partition and Swap 
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
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
        
        System.out.println("Starting execution...");
        QuickSort ob = new QuickSort(); 
        ob.partition(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
