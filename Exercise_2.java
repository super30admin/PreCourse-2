// Time Complexity : O(nlog n)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this : no


/*Your code here along with comments explaining your approach
partition the array by setting the last element as a pivot, put all smaller elements on left side of pivot and larger elements on the right side of pivot
sort the left sub array and right sub array recursively.
*/



class Exercise_2 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here   
    	int temp =arr[i];
    	arr[i]=arr[j];
    	arr[j]=temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    	int pivot= arr[high];
    	int r=low-1;
    	for(int i=low;i<=high-1;i++) {
    		if(arr[i]<pivot) {
    			r++;
    			swap(arr,r,i);
    		}
    	}
    	swap(arr,r+1,high);
    	return(r+1);
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
    	if(low<high) {
    		int p= partition(arr,low,high);
    		sort(arr,low,p-1);
    		sort(arr,p+1,high);
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
  
        Exercise_2 ob = new Exercise_2(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
