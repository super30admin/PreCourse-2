class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    static void swap(int arr[],int i,int j){
        //Your code here
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;		
    }
    
    static int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
		int pivot = arr[high];
		int i = (low - 1);
 
		for(int j = low; j <= high - 1; j++)
		{
			if (arr[j] < pivot)
			{
            i++;
            swap(arr, i, j);
			}
		}
    swap(arr, i + 1, high);
    return (i + 1);
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    static void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before 
        // partition and after partition 
		if (low < high)
		{
			int pi = partition(arr, low, high);
			sort(arr, low, pi - 1);
			sort(arr, pi + 1, high);
		}
			
    } 
  
    static void printArray(int arr[], int size) 
    { 
        for(int i = 0; i < size; i++)
		{
			System.out.print(arr[i] + " ");
		}
		System.out.println();
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int[] arr = { 10, 7, 8, 9, 1, 5 };
		int n = arr.length;
     
		sort(arr, 0, n - 1);
		System.out.println("Sorted array: ");
		printArray(arr, n); 
    } 
}  
