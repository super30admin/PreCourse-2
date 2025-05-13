// Time complexity : O(n log n)
//Space complexity : O(log n)
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
        //Your code here   
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
   	    int p = arr[high];
   	     int i = low - 1; // index of smaller element

        for (int j = low; j < high; j++) {
            if (arr[j] <= p) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);

        return i + 1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low < high) {
            int pi = partition(arr, low, high);

            // Recursively sort elements before and after partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
            // Recursively sort elements before 
            // partition and after partition 
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
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
