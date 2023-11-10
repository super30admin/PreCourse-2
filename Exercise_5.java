class IterativeQuickSort {
    //Time Complexity :- O(nlogn)
    //Space Complexity :- O(n)
    void swap(int arr[], int i, int j) 
    { 
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    } 

    int partition(int arr[], int l, int h) 
    { 
        int x = arr[h];
        int i = (l - 1);
        
        for (int j = l; j <= h - 1; j++) {
        if (arr[j] <= x) {
            i++;
            swap(arr, i, j);
        }
        }
        swap(arr, i + 1, h);
        return (i + 1);
        
    } 
  
    void QuickSort(int arr[], int l, int h) 
    { 
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