class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int a[], int i, int j){
        //Your code here
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    
    int partition(int a[], int low, int high)
    { 
   	//Write code here for Partition and Swap
        int i, j, p;
        p = a[high];
        i = low - 1;
        for(j = low; j < high; j++) {
            if(a[j] < p) {
                i++;
                swap(a, i, j);
            }
        }
        i++;
        swap(a, i, high);
        return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void quicksort(int a[], int low, int high)
    {  
            // Recursively sort elements before 
            // partition and after partition
        if(low < high) {
            int p = partition(a, low, high);
            quicksort(a, low, p - 1);
            quicksort(a, p + 1, high);
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