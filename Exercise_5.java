class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
        
        //No need to swap when there are repeated elements
        if(arr[i] == arr[j])
            return;
        
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
        int lower = l - 1;
        for(int i = l; i <= h-1; i++)
        {
            if(arr[i] <= pivot)
            {
                lower++;
                swap(arr,lower,i);
            }
        }
        swap(arr,lower+1,h);
        return lower+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];
        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while(top >= 0)
        {
            h = stack[top--];
            l = stack[top--];

            int pivot = partition(arr,l,h);

            if(l < (pivot - 1))
            {
                stack[++top] = l;
                stack[++top] = pivot - 1;

            }

            if((pivot + 1) < h)
            {
                stack[++top] = pivot + 1;
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