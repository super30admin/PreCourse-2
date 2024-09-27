import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
       
          if(i != j) {
          
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }  
     } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int p_index = h;

        for(int i = h-1; i>=l ; i-- )
        {
            if( arr[i] > pivot )
                swap( arr, i, --p_index );
        }
        swap(arr, p_index, h);
        return p_index;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);
        stack.push(-1);

        while (!stack.isEmpty()) {

            while (low <= high) {

                int p_index = partition(arr, low, high);
                stack.push(high);
                stack.push(p_index+1);
                high = p_index-1;
            }
            low = stack.pop();
            high = stack.pop();
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