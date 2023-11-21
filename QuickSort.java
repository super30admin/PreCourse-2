/*
T.C O(nlog n)
S.C O(1)
 */
class QuickSort
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */

    int partition(int arr[], int low, int high) 
    {
   	//Write code here for Partition and Swap
        int pivot = arr[low];
        int i = low;
        int j = high;
        //{10, 7, 8, 9, 1, 5};
        while(i<j) {
            while (i < j && arr[--j] >= pivot) ;

            if (i < j) {
                arr[i] = arr[j];
            }

            while (i < j && arr[++i] <= pivot) ;
            if (i < j) {
                arr[j] = arr[i];
            }
        }
        arr[j] = pivot;
        return j;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        if(high - low < 2)
            return;
            // Recursively sort elements before 
            // partition and after partition
        int pivotIndex = partition(arr, low, high);
        sort(arr, low, pivotIndex);
        sort(arr, pivotIndex + 1, high);
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
        int arr[] = { 4, 3, 5, 2, 1 };
        int n = arr.length;
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n);
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
