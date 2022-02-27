/**
 * Implemented the sort in ascending order
 * 
 * Space complexity is O(n) as sorting is happening in place.
 * 
 * Time complexity - best case scenario it is O(n) when all the elements are already sorted.
 * worst case scenario is O(n*n) when the elements are in descending order.
 */
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
       int i = low;
       int j = high;
       int pivot = arr[low];
       while(i < j) {

           while(i < arr.length && arr[i] <= pivot) {
               i++;
           }

           while(arr[j] > pivot) {
               j--;
           }
           if(i < j)
           swap(arr, i, j);
       }
       swap(arr, j, low);
       
       return j;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            System.out.println(low);
            System.out.println(high);
            System.out.println("----------");
            if (low < high) {
                int pivotIndex = partition(arr, low, high);
                sort(arr, low, pivotIndex);
                sort(arr, pivotIndex+1, high);
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
        int arr[] = {10, 7, 8, 9, 1, 5, 2, -1}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
