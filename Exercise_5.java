class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if(i != j) // if indexes are same no need to swap. 
        {
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
        int left = l, right = h;
        int pivot = arr[h];
        
        while (left < right)
        {
            while(arr[left] <= pivot && left < right)
            {
                left++;
            }
            while(arr[right] >= pivot && left < right)
            {
                right--;
            }
            swap(arr, left, right);
        }
        swap(arr, left, h);
        return left;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        
        int[] stack = new int[h-l+1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;
        
        while(top > 0)
        {
            h = stack[top--];
            l = stack[top--];
            
            int partitionIndex = partition(arr, l, h);
            
            if(l < partitionIndex-1 )
            {
                stack[++top] = l;
                stack[++top] = partitionIndex-1;
            }
            if(partitionIndex+1 < h )
            {
                stack[++top] = partitionIndex+1;
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
            System.out.println(""); 
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