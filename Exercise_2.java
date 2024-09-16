class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int[] arr, int i, int j){
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int[] arr, int low, int high)
    {
        //Write code here for Partition and Swap
        int pivotIndex = high;

        // Collects all the elements which are smaller than pivot.
        // Keeps track of the Most significant index associated to the smaller element.
        int i = low-1;

        // compare all the elements in the array against pivot
        for(int j = low; j <= pivotIndex-1; j++){

            // If current element is less than pivot throw it back to i.
            if(arr[j] < arr[pivotIndex]){
                i++;
                swap(arr, i, j);
            }
        }

        // once all the elements in the current iteration are organised, swap the pivot element with index next to i.
        // i pointer contains only the elements lesser than pivot.
        swap(arr, i+1, pivotIndex);

        // return the index at which pivot is stored.
        return (i+1);
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int[] arr, int low, int high)
    {
        // Recursively sort elements before
        // partition and after partition
        if(low < high){
            int pivot = partition(arr, low, high);
            sort(arr, low, pivot-1);
            sort(arr, pivot+1, high);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String[] args)
    { 
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
