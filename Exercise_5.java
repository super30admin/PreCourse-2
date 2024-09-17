// Time Complexity : worst case o(n^2), average case o(n logn)
// Space Complexity : worst case o(n) considering stack usage
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
	    	int p = arr[high];
			int l = low;
			
			for (int i = low; i < high; i++) {
				if(arr[i] < p) {
					int temp = arr[l];
					arr[l] = arr[i];
					arr[i] = temp;
					l++;
				}
			}
			
			int temp = arr[l];
			arr[l] = arr[high];
			arr[high] = temp;
			
			return l;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    		int[] stack = new int [h-l+1];
    		int stackTop = -1;
    		
    		stack[++stackTop] = l;
    		stack[++stackTop] = h;
    		
    		while(stackTop > -1) {
    			int high = stack[stackTop--];
    			int low = stack[stackTop--];
    			
    			int p = partition(arr, low, high);
    			
    			if(p - 1 > low) {
    				stack[++stackTop] = low;
    				stack[++stackTop] = p - 1;
    			}
    			
    			if(p + 1 < high) {
    				stack[++stackTop] = p + 1;
    				stack[++stackTop] = high;
    			}
    		}
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3, 6 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 