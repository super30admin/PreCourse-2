// Time Complexity : O(nlog n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this : yes, how to stop recursion

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
        arr[i] =arr[j];
        arr[j]=temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap

        int q=arr[high];
        int i=low-1;
        for(int j=low;j<=high;j++)
        {
            if(q>arr[j])
            {
                i++;
                swap(arr, i, j);
            }
        }
//        System.out.println();
//        System.out.println("high "+high+" low "+low);
        swap(arr,i+1,high);
//        printArray(arr);
        return i+1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        if(low<high)
        {
            // Recursively sort elements before
            // partition and after partition

            int q = partition(arr, low, high);
            sort(arr, low, q-1);
            sort(arr,q+1, high);
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
