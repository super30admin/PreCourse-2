/* Time Complexity : 
 * 	arr - O(n log n) - due to partition + recursion
 * 	arr2, arr3, arr4 - O(n^2) - already sorted or reverse
 * */
/* Space Complexity : 
 * 	arr - O(log n) - due to recursion
 * 	arr2, arr3, arr4 - O(n) - already sorted or reverse
 * */
// Did this code successfully run on Leetcode : -
// Any problem you faced while coding this : -

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
    	int temp = arr[i];
    	arr[i] =arr[j];
    	arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    {	 
   	//Write code here for Partition and Swap
    	int pivot = arr[high];
    	int i = low-1;
    	
    	for(int j = low; j< high; j++) {
    		if(arr[j] <= pivot) {
    			i++;
    			swap(arr, i, j);
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
    	if(arr.length > 0) {
            // Recursively sort elements before 
    		if(low < high) {
    			// partition and after partition 
    			int p = partition(arr, low, high);
    			sort(arr, low, p-1);
    			sort(arr, p+1, high);
    		}
    	}
    	else {
    		System.out.println("Empty array");
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
        
        int arr2[] = {10 ,1}; 
        int n2 = arr2.length; 
  
        ob.sort(arr2, 0, n2-1); 
  
        System.out.println("sorted array"); 
        printArray(arr2);
        
        int arr3[] = {1 ,10}; 
        int n3 = arr3.length; 
  
        ob.sort(arr3, 0, n3-1); 
  
        System.out.println("sorted array"); 
        printArray(arr3);
        
        int arr4[] = {1 ,-10}; 
        int n4 = arr4.length; 
  
        ob.sort(arr4, 0, n4-1); 
  
        System.out.println("sorted array"); 
        printArray(arr4);
    } 
} 
