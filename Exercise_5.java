//Time Complexity O(nlogn)
//Space Complexity O(logn)

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    	if(i!=j) {
	//Try swapping without extra variable 
    	i = i + j;
        j = i - j;
        i = i - j;
      
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot = arr[h]; 
        int i = l - 1; 
        for (int j = l; j < h; j++) { 
            if (arr[j] <= pivot) { 
                i++; 
                swap(arr, i, j); 
            } 
        } 
        swap(arr, i + 1, h); 
        return i + 1; 
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<Integer> stack = new Stack<>(); 
    	  
        // Push initial values
        stack.push(l); 
        stack.push(h); 
  
        // Pop until stack is empty
        while (!stack.isEmpty()) { 
            h = stack.pop(); 
            l = stack.pop(); 
  
            int p = partition(arr, l, h); 
  
            // Push left subarray indices
            if (p - 1 > l) { 
                stack.push(l); 
                stack.push(p - 1); 
            } 
  
            // Push right subarray indices
            if (p + 1 < h) { 
                stack.push(p + 1); 
                stack.push(h); 
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