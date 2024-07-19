class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        //Try swapping without extra variable 
        if (i == j || arr[i] == arr[j] ) {
            // No need to swap
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
        int pivot = arr[(l + h)/2];

        while (l <= h) {
            while (arr[l] < pivot) {
                l ++;
            }

            while (arr[h] > pivot) {
                h --;
            }

            if (l <= h) {
                swap(arr, l, h);
                l ++;
                h --;
            }
        }
        return l;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 

        java.util.Stack<Integer> stack = new java.util.Stack<>();
        //Try using Stack Data Structure to remove recursion.

        stack.push(l);
        stack.push(h);

        while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();

            int index = partition(arr, l, h);

            if (l < index - 1) {
                stack.push(l);
                stack.push(index - 1);
                // QuickSort(arr, l, index - 1);
            }
    
            if (index < h) {
                stack.push(index);
                stack.push(h);
                // QuickSort(arr, index, h);
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
        // int arr[] = { 4, 0, 5, 2, 1, 3, 8, 9 };  
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 