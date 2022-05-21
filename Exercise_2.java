// Time Complexity :O(nlogn)
// Space Complexity :O(n) no. of elements in the stack at time of recurrsion.
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
        return;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
        int pivot = arr[high];// making last element the pivot
        int low_pointer = low;// starting a pointer from low
        for (int i = low; i <= high - 1; i++) {// swapping lowPtr with pivot if element at j is smaller than pivot
            if (arr[i] <= pivot) {
                swap(arr, low_pointer, i);
                low_pointer++;
            }
        }   
        swap(arr, lowptr, high);
        return lowptr;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
        if (low >= high)
            return;
        int ptr = partition(arr, low, high);
        sort(arr, low, ptr - 1);
        sort(arr, ptr + 1, high);
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
        QuickSort ob1 = new QuickSort();
        int arr1[] = { 4, 2, 1, 3, 5, 2, 3, 2 };
        ob1.sort(arr1, 0, arr1.length - 1);
        printArray(arr1);
    } 
} 
