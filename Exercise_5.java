class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        if(arr[i] != arr[j]) {
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
        int pivot = h;
        int idx = l;

        for(int i = l ; i < h; i++) {
            if(arr[i] <= arr[pivot]) {
                swap(arr, idx, i);
                idx++;
            }
        }

        swap(arr, idx, pivot);

        return idx;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h)
    {

        //Try using Stack Data Structure to remove recursion.
        int stack[] = new int[h - l + 1];

        // initialize top of stack
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;

        while(top >= 0){
            h = stack[top--];
            l = stack[top--];
            int pa = partition(arr, l, h);

            if (pa - 1 > l) {
                stack[++top] = l;
                stack[++top] = pa-1;
            }
            if (pa + 1 < h) {
                stack[++top] = pa+1;
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