import java.util.Stack;

class IterativeQuickSort { 
	void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
	  
    	arr[i] = arr[i] + arr[j];
    	arr[j] = arr[i] - arr[j];
    	arr[i] = arr[i] - arr[j];
    	
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int lowIndex = l;
    	int pivot = h;
    	
    	for(int i=l; i<=pivot; i++) {
    		if(arr[i] < arr[pivot]) {
    		    if(lowIndex != i){
    		        swap(arr, lowIndex, i);    
    		    }
    			
    			lowIndex = lowIndex + 1;
    		}
    	}
    	
    	if(lowIndex != pivot)
    	    swap(arr, lowIndex, pivot);
    	return lowIndex;
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
    		
    		if(low < high) {
    			int partitionIndex = partition(arr, low, high);
    			stack.push(low);
    			stack.push(partitionIndex-1);
    			
    			stack.push(partitionIndex + 1);
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