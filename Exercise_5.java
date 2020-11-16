class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int greatest = arr[h]; 
        int i = (l - 1); 
        for (int j = l; j <= h - 1; j++) { 
            if (arr[j] <= greatest) { 
                i++; 
  
                // swap arr[i] and arr[j] 
                swap(arr, i, j); 
            } 
        } 
  
        // swap arr[i+1] and arr[high] (or pivot) 
        swap(arr, i + 1, h);  
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int stack[] = new int[h - l + 1]; 
        int top = -1;  
        stack[++top] = l; 
        stack[++top] = h; 
        while (top >= 0) { 
          
            h = stack[top--]; 
            l = stack[top--]; 
            int p = partition(arr, l, h); 
            if (p - 1 > l) { 
                stack[++top] = l; 
                stack[++top] = p - 1; 
            }
            if (p + 1 < h) { 
                stack[++top] = p + 1; 
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
