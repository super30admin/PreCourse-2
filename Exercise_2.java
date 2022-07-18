// Time Complexity : O(nlogn) as we use divide and conquer
// Space Complexity : O(logn) we are doing inplace but using recursive call stack
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : yes needed to refer how does quick sort work


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
    
    int partition(int low, int high, int arr[]) 
    { 
   	 int i= low-1;
    int pivot = arr[high];
    for(int j=low;j<=high-1;j++) {
        if(arr[j]<=pivot) {
            i++;
            swap(arr,i,j);
        }
    }
    i=i+1;
    swap(arr,i,high);
    return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int low, int high, int arr[] ) 
    {  
        if(low>=high)
        return;
        int p = partition(low, high, arr);
        sort(low,p-1,arr);
        sort(p+1,high,arr); 
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
        ob.sort(0, n-1, arr); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
