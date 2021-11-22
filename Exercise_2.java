
/*
 * * Time Complexity: O(n^ 2)
 * 
 * Space Complexity: O(n)
 * 
 * This code will run successfully on Leetcode
 * 
 * Any problems you face while coding this - No
 * 
 * Approach: 
 * 1. find pivot of array (element at index high).
 * 2.put all elements lower than pivot to left of pivot by swapping. once done, put element at high at next index
 * 3. this way me know that pivot is in the right position as in all elements to its left are lower than pivot
 * 	  and all elements to its right are greater than pivot.
 * 4. Now sort all elements at its left, then same to right.
 * 5. In each case we put respective element at its correct index which gives us sorted array
 
 *
 */
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
   	//Write code here for Partition and Swap 
    	
    	int pivot = arr[high];
    	int i = low - 1;
    	
    	for(int j = low; j < high;j++) {
    		if(arr[j] <= pivot) {
    			i++;
    			swap(arr, i, j);
    		}
    	}
    	
    	i++;
    	swap(arr, i, high);
    	return i;
    } 
    
    
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
    		if(low < high) {
    			int index = partition(arr, low, high);
        		
        		this.sort(arr, low, index-1);
        		this.sort(arr, index+1, high);
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