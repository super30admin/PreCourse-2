class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    	int pivot = high; //setting the last element as pivot
    	int i = low;
    	for(int j=low;j<high;j++)
    	{
    		if(arr[j]<=arr[pivot])
    		{
    			swap(arr,i,j); 
    			i++;
    		}
    	}
    	swap(arr,i,pivot);
    	return i;
    } 
  
    void swap(int arr[], int i, int j)
    {
    	int temp = arr[i];
    	arr[i] = arr[j];
    	arr[j] = temp;
    }
  
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
    	if(low<high)
    	{
    		int p = partition(arr,low,high);
    		
    		sort(arr,low,p-1); //recursively sort left of partition
    		sort(arr,p+1,high); //recursively sorting right of partition
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
        int arr[] = {10, 20, 30, 40, 50,60,70}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 