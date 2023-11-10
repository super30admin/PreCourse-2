// Time Complexity : O(N^2)
// Space Complexity : O(1)

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        if (arr[i] == arr[j])
            return;

        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }
    
    int partition(int arr[], int low, int high) 
    { 
        // choose high as pivot
   	    int pivot = arr[high];

        // initialize partition index
        int i = low - 1;

        // put all elements lower than pivot to left of pivot
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // put pivot into correct position
        swap(arr, i + 1, high);

        // return index of sorted element (pivot)
        return i + 1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
        if (low < high) {
            int pIndex = partition(arr, low, high);
            sort(arr, low, pIndex - 1);
            sort(arr, pIndex + 1, high);
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
