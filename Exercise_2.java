class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
	
	//Approach: Here there are 3 functions, 
	//swap - to swap elements in the array
	//partition - choose a pivot element , here am choosing last element as pivot 
	// and rearrange the array such that elements less than pivot comes before it and element 
	// higher than it goes after it in the array.
	//sort - sorting is done recursively to separate elements into halves
    void swap(int arr[],int i,int j){
        //Your code here   
    	int temp = arr[i];
    	arr[i] = arr[j];
    	arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
    	int i=(low-1);
    	int pivot = arr[high];
    	for(int j=low ; j <= high-1 ;j++)
    	{
    		if(arr[j] < pivot)
    		{
    			i++;
    			swap(arr,i,j);
    		}
    	}
    	swap(arr, i+1, high);
    	return (i+1);
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
    	printArray(arr);
            // Recursively sort elements before 
            // partition and after partition 
    	if(low < high)
    	{
    		int partition = partition(arr,low, high);
    		sort(arr, low, partition-1);
    		sort(arr, partition+1, high);
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

//Time Complexity : O(n2), since by worst case we might end up choosing the pivot wrongly such that
//the partition might end up resulting in n-1 elements and 1 element halves. In this case we have to sorting 
// for althose n-1 elements all over again.
//Space Complexity : O(1) no extra space is used
//Did this code successfully run on Leetcode : NA
//Any problem you faced while coding this : 
