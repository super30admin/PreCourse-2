class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
       // O(NlogN) average time and O(N^2) worst case time complexity
       //O( N ) recursive calls
    void swap(int arr[],int i,int j){
        //swap values at indices i and j in-place  
      if(i != j) {
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i]-arr[j];
        arr[i] = arr[i]-arr[j];
      }
    }
    
    int partition(int arr[], int low, int high) 
    { 
          //Pivot is the element in index high
          int i = low-1;
          int pivot = arr[high];
          
          //If element at index j is less than pivot, swap j and i index elements
          for(int j = low; j < high; j++) {
              if(arr[j] <= pivot) {
                i++;
                swap(arr,i,j);
              }
          }
          swap(arr,i+1,high);
          return i+1;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
          if(low < high) {
              int partitionIndex = partition(arr, low, high);
              //call sort recursively on the partitions till low >= high
              sort(arr,low,partitionIndex-1);
              sort(arr,partitionIndex+1,high);
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
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3 }; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
