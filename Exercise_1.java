class QuickSort 
{ 
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high]; 
        int i = (low - 1);  // Index of smaller element
        for (int j = low; j < high; j++) {
            // If current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    } 
    
    void sort(int arr[], int low, int high) 
    {  
        if (low < high) {
            int pi = partition(arr, low, high);  // Partitioning index

            // Recursively sort elements before and after partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    } 
  
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("Sorted array"); 
        printArray(arr); 
    } 
}
