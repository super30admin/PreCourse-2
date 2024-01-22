class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            while(low > high) {
                return;
            }

            int start = low;
            int end = high;
            int mid = low + (high - low) / 2;

            int pivotElement = arr[mid];

            while(low <= high) {

                if(arr[low] >= pivotElement && arr[high] <= pivotElement) {
                    swap(arr, low, high);
                    low++;
                    high--;
                } else if(arr[low] <= pivotElement) {
                    low++;
                } else if(arr[high] >= pivotElement) {
                    high--;
                }
            }
        sort(arr, low, end);
        sort(arr, start, high);
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
        int arr[] = {10, 8, 20, 4, 40, 90, 2};
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
