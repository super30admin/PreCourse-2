//Time complexity: best+average case: O(nlogn) worst case: O(n^2)
//Space complexity: best+average case: O(logn) worst case: O(n) //for recursive stack
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
        if(high==low){
            return low;
        }
        int pivot = arr[high], pivotIndex = high;
        int i = low, j = high-1;
        while(i<=j){
            while(i<=high-1 && arr[i]<=pivot){
                i++;
            }
            while(j>=low && arr[j]>=pivot){
                j--;
            }
            if(i<j){
                swap(arr, i,j);
            }
        }
        swap(arr, pivotIndex, j+1);
        return j+1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before 
        if(low<high){
            int part = partition(arr, low, high);
            sort(arr, low, part-1);
            sort(arr, part+1, high); 
        }
        // partition and after partition 
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
        //int arr[] = {7, 6, 5, 4, 3, 2, 1};
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
