
// Time Complexity : O(nlogn)
// Space Complexity :O(logn)
// Any problem you faced while coding this : Was unable to implement, had to take a lot of help from internet
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 

        int temp= arr[i];
        arr[i]= arr[j];
        arr[j]= temp;
        // arr[i]=arr[i]+arr[j];
        // arr[j]= arr[i]-arr[j];
        // arr[i]= arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot= arr[h];
    	// Keeping the pointer one index before the starting index 
    	int pointer = l - 1; 
        
    	
    	for (int i= l; i<=h-1; i++) {
    		if (arr[i]<pivot) {
    			pointer++;
    			swap(arr,pointer, i);
    		}
    	
            
    	}
    	swap(arr, pointer+1, h);
        
    	return pointer+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        // Init stack

        int stack[] = new int[h - l + 1];
 
        // create top pointer
        int top = -1;
        // add l and h to stack
        stack[++top] = l;
        stack[++top] = h;
 
        // keep popping elements until stack is not empty
        while (top >= 0) {
        // pop h and l
        h = stack[top--];
        l = stack[top--];
        
        // find the split point
        int splitPoint = partition(arr, l, h);
        
            // add left elements to stack
        if (splitPoint - 1 > l) {
            stack[++top] = l;
            stack[++top] = splitPoint - 1;
        }
        
        // add right elements to stack
        if (splitPoint + 1 < h) {
            stack[++top] = splitPoint + 1;
            stack[++top] = h;
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 

   
