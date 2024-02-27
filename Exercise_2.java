class Exercise_2 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[], int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[low];
        int i = low;
        int j = high;
        while (i < j) {
            // Move i to the right until we find an element larger than the pivot
            while (i <= high && arr[i] <= pivot)
                i++;
            // Move j to the left until we find an element smaller than the pivot
            while (arr[j] > pivot)
                j--;
            // If i and j have not crossed each other swap the elements at i and j
            if (i < j)
                swap(arr, i, j);
        }
        // Swap the pivot element with the element at index j
        swap(arr, low, j);
        // Return the partition index
        return j;
    } 

    /* The main function that implements QuickSort() 
       arr[] --> Array to be sorted, 
       low  --> Starting index, 
       high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low < high) {
            // Find pivot element such that
            // elements smaller than pivot are on the left
            // elements greater than pivot are on the right
            int pi = partition(arr, low, high);
            
            // Recursively sort elements before partition and after partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
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
