import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    		if(i == j) {
    			return;
    		}
    		arr[i] = arr[i] + arr[j];
    		arr[j] = arr[i] - arr[j];
    		arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
		int pivot = arr[h];
		int ptr = l;
		for(int i=l; i<h; i++) {
			if(arr[i] <= pivot) {
				swap(arr, i, ptr);
				ptr++;
			}
		}
		swap(arr, h, ptr);
		return ptr;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
    		//Try using Stack Data Structure to remove recursion.
    		Stack<Integer> stack = new Stack<Integer>();
    		stack.push(l);
    		stack.push(h);	
    		
    		while(!stack.isEmpty()) {
    			int high = stack.pop();
    			int low = stack.pop();
    			
    			int pi = partition(arr, low, high);
    			
    			//Push left part only if there are no elements towards left of pivot
    			if(pi - 1 > low) {
    				stack.push(low);
        			stack.push(pi-1);
    			}
    			
    			//Push right part only if there are no elements towards right of pivot
			if (pi + 1 < high) { 
				stack.push(pi+1);
	    			stack.push(high);
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