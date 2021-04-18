class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = array[h]; // Choosing the Last Element as Pivot

        int small = (l-1);
        for (int big = l; big<h; big++){
            
            if (arr[big] < pivot){
                small++;
                swap(arr, big, small); // All Elements Greater than Pivot should be to the Right of the Pivot's Position
            }
        }

        swap(arr, small+1, h); // Small is the last element in the rray that is less than pivot. 
                               // Swapping Small+1 Element with Pivot 
                               // to ensure all elements after pivot is greater than pivot 
                               // And all elements less that pivot is less than pivot.
        return small+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.

        if (l<h) {
            int partition = partition(arr, l, h);
            QuickSort(arr, l, partition-1);
            QuickSort(arr, partition+1, h);
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