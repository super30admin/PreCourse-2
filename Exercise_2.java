//complexity
// Time: worst case: O(n^2); avg: O(n log n)
//Space: O(n) for recursive calls (implicit)

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
    	int pivot = arr[high];
    	int i = low;
    	
    	for(int j = low; j < high; j++) {
    		//swap if current is smaller than pivot
    		if(arr[j] < pivot) {
    			swap(arr, i, j);
    			i++;
    		}
    	}
    	//now swap pivot and arr[i]
    	swap(arr, i, high);
    	
    	//return position of pivot
    	return i;
    	
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        //base
    	if(low >= high) return;
    	
    	//get pivot position and sort around it
    	int pivotInd = partition(arr, low, high);
    	sort(arr, low, pivotInd - 1);
    	sort(arr, pivotInd + 1, high);
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
