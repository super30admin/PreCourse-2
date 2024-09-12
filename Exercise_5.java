class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        i = i ^ j;
        j = i ^ j;
        i = i ^ j;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int boundary = l - 1;

        for (int i=l; i<=h; i++) {
            if (arr[i] <= pivot) {
                boundary++;
                swap(arr, i, boundary);
            }
        }
        return boundary;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) {
        //Try using Stack Data Structure to remove recursion.
        int list[] = new int[h - l + 1];
        int top = -1;
        list[++top] = l;
        list[++top] = h;
        while (top >= 0) {
            h = list[top--];
            l = list[top--];
            int boundary = partition(arr, l, h);
            if (boundary - 1 > l) {
                list[++top] = l;
                list[++top] = boundary - 1;
            }
            if (boundary + 1 < h) {
                list[++top] = boundary + 1;
                list[++top] = h;
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