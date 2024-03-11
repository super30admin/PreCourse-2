//TC: O( N log (N)) average case, O(N*N) worst case when When the array is already sorted and the pivot is always chosen as the smallest or largest element.
//SC: O(1)
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here   
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    int pivot = arr[high];
    int i = low;
    for(int j = low; j< high; j++){
        if(arr[j]<=pivot){
            swap(arr, i, j);
            i = i+1;
        }
        swap(arr, i, high);
    }
    return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low < high) {
            //This line puts the pivot element in the right place
            int pivotIndex = partition(arr, low, high);
            //This calls sort method on left subarray until array is reduced to single element
            sort(arr, low, pivotIndex - 1);
            //This calls sort method on right subarray
            sort(arr, pivotIndex + 1, high);
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
