
// Time Complexity : O(nlogn)
// Space Complexity :O(logn)
// Any problem you faced while coding this : Was unable to implement, had to take a lot of help from internet


// Your code here along with comments explaining your approach

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
        int temp= arr[i];
        arr[i]= arr[j];
        arr[j]= temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    	int pivot= arr[high];
    	// Keeping the pointer one index before the starting index 
    	int pointer = low - 1; 
        
    	
    	for (int i= low; i<=high-1; i++) {
    		if (arr[i]<pivot) {
    			pointer++;
    			swap(arr,pointer, i);
    		}
    	
            
    	}
    	swap(arr, pointer+1, high);
        
    	return pointer+1;
    	
  

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
    	 if(low<high) {
    		 int splitPoint= partition(arr, low, high);
    		 
    		 sort(arr, low, splitPoint-1);
    		 sort(arr, splitPoint+1, high);
    	 }
    } 
  

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[]) {
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
        QuickSort ob1 = new QuickSort();
        int arr1[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob1.sort(arr1, 0, arr1.length - 1);
        printArray(arr1);
    }
}
