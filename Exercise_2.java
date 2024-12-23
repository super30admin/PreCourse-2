class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
       // Time Complexity: O(n log(n)) (average case)
       // Time Complexity: O(n^2) (worst case)
    void swap(int arr[], int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        
    }
    
    int partition(int arr[], int low, int high) 
    { 
        //chose pivot 
        int pivot = arr[low];
        int i = low+1, j = high-1;
        while (true) {
           while (i < high -1 && arr[i] < pivot){
                i++;
            }
           while (j > low && arr[j] > pivot){
                j--;
            }
           if (i >= j){
            break;
           } 
           swap(arr, i, j);
           i++;
           j--;
        }
        swap(arr, low, j);
        return j;
   	//Write code here for Partition and Swap 
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low < high) {
            int p = partition(arr, low, high);
            sort(arr, low, p);
            sort(arr, p+1, high);
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
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        System.out.println("Original array: ");
        printArray(arr);
        ob.sort(arr, 0, n); 
        
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
