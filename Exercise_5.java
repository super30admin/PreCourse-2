class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if( i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }

        //Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
       int partition(int arr[], int low, int high)
       {
           int pivot = arr[high];
    
           // index of smaller element
           int i = (low - 1);
           for (int j = low; j <= high - 1; j++) {
               // If current element is smaller than or
               // equal to pivot
               if (arr[j] <= pivot) {
                   i++;
    
                   // swap arr[i] and arr[j]
                   swap(arr, i, j);
               }
           }
    
           // swap arr[i+1] and arr[high] (or pivot)
           swap(arr, i+1, high);
    
           return i + 1;
       }
    
       /* A[] --> Array to be sorted,
      l  --> Starting index,
      h  --> Ending index */
       void quickSortIterative(int arr[], int l, int h)
       {
           // Create an auxiliary stack
           int[] stack = new int[h - l + 1];
    
           // initialize top of stack
           int top = -1;
    
           // push initial values of l and h to stack
           stack[++top] = l;
           stack[++top] = h;
    
           // Keep popping from stack while is not empty
           while (top >= 0) {
               // Pop h and l
               h = stack[top--];
               l = stack[top--];
    
               // Set pivot element at its correct position
               // in sorted array
               int p = partition(arr, l, h);
    
               // If there are elements on left side of pivot,
               // then push left side to stack
               if (p - 1 > l) {
                   stack[++top] = l;
                   stack[++top] = p - 1;
               }
    
               // If there are elements on right side of pivot,
               // then push right side to stack
               if (p + 1 < h) {
                   stack[++top] = p + 1;
                   stack[++top] = h;
               }
           }
       }

    void printArr(int arr[], int h) {
        for (int i = 0; i < h; i++) {
            System.out.print(arr[i] + ", ");
        }
       }
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.quickSortIterative(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 