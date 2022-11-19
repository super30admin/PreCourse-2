//Time Complexity : Best case is when the pivot element is the middle element in the sorted array, then O(nlogn). Otherwise it would be O(n^2) in the worst case
//Space Complexity :
//This implementation is recursive , which means there will be call stack that can take additional space. 
//At worst we may have to recurse till O(n) times (when array is already sorted and we are picking last/first element as the pivot)
// In the best case scenario, if the pivot is the middle element of the sorted array, then space would be O(logn)
//Did this code successfully run on Leetcode :
//Any problem you faced while coding this : yes, partitioning logic was hard to understand first


//Your code here along with comments explaining your approach


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
    	
    	int temp = arr[j];
    	arr[j] = arr[i];
    	arr[i] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    	
    	int pivot  = arr[high]; // taking last element as pivot
    	int i = low -1; // i is the index where smaller values should be. decrementing by one so that we can preserve the index of pivot in the sorted array after the iterations are finished
    	
    	// We will put all the values smaller than pivot on the left side of the pivot in the sorted array
    	// The larger values would then be remain on the right side of the pivot
    	
    	for(int j=low;j<=high;j++) { // j<= high , so that we can scan element till high, and at the end of the iteration, the pivot would find its perfect position
    		if(arr[j] <= pivot) { 
    			// We have found the next smaller element 
    			// so we advance the index by one, as if any previous value i was pointing to, then it will be point to the next available place the the next smaller item 
    			// should b
    			i++;    			
    			// Swapping i with J , as j is pointing to the next small value and i is pointing to the index where the next small value should b
    			swap(arr,i,j);
    		}
    	}
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
    	int pivotPosition = partition(arr,low,high);
    	// will not include the partition
    	// sort elements before partition
    	sort(arr,low,pivotPosition-1); 
    	
    	//sort elements after partition
    	sort(arr,pivotPosition+1,high);
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