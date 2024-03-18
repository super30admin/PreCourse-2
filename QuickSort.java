/*
 * Time complexity - O(n^2) for worst case and O(n*logn) for average case
 * Space complexity - O(n*logn)
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
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
        if(low < 0 || high < 0) return -1;
        int pivot = low;
        int i=low+1; int j=high;
        while(i < j) {
            while(arr[i] <= arr[pivot] && i < j) {
                i++;
            }
            while(arr[j] > arr[pivot] && i <= j) j--;
            if(i < j) swap(arr, i, j);
        }
        System.out.println("pivot, j " + arr[pivot] + " " + arr[j]);
        swap(arr, pivot, j);
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
        if(low >= high) return;
        int j = partition(arr, low, high);
        
        sort(arr, low, j-1);
        sort(arr, j+1, high);
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
