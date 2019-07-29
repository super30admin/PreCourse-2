/**
 * Time Complexity: 
 * Worst Case: Occurs when a smallest or largest element always gets picked as pivot 
 * => T(0)+T(n-1)+O(n) 
 * => T(n-1)+O(n)
 * => O(n^2)
 * Avg Case: nlogn
 * Space Complexity: log n
 */
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
    		int ptr = low;
    		for(int i=low; i<high; i++) {
    			if(arr[i] <= pivot) {
    				swap(arr, i, ptr);
    				ptr++;
    			}
    		}
    		swap(arr, ptr, high);
    		return ptr;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    
    static void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
    		if(low < high) {
    			int pi = partition(arr, low, high);
    			sort(arr, low, pi-1);
    			sort(arr, pi+1, high);
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
