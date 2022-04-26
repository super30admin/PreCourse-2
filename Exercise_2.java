class QuickSort {
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[], int i, int j) {
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        //Write code here for Partition and Swap
        int pivot = arr[high];
        int l = low;
        int r = high - 1;
        while (l < r) {
            while (arr[l] <= pivot && l < r) {
                l++;
            }
            while (arr[r] >= pivot && l > r) {
                r--;
            }
            swap(arr, l, r);
        }
        if (arr[l] > arr[high]) {
            swap(arr, l, high);
        } else {
            l = high;

        }
        return l;
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) {
        if (low >= high) {
            return;
        }
        if (low < high) {
            int r = partition(arr, low, high);
        }
        // Recursively sort elements before
        // partition and after partition
        sort(arr, low, r - 1);
        sort(arr, r + 1, high);
    }

}
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
