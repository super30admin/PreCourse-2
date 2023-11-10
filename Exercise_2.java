// Time Complexity :
    //worst case : O(n^2) - since we took the last element as the pivot here, if the pivot is the smallest/largest element of the list. This will happen if the array is already sorted in an ascending/descending order
                // n + (n-1) + (n-2) .... 1
    //avg case: O(nlogn): time taken by the partition() method for each call will be ~n as we have to traverse through the entire list;
                            // and assuming that we divide the list in halves in an avg case, it will be log(n)
                            // n * log(n) = O(nlog(n))
// Space Complexity : since this is a recursive algo, it'll use a stack and the size of the stack will depend on "height" of the tree that will be created after each partition
    //which can range from log(n) to n (if the list is already sorted).
// Did this code successfully run on Leetcode :N/A
// Any problem you faced while coding this :

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
        //Write code here for Partition and Swap
        int pivot = arr[high];
        int i = low-1;

        for(int j = low; j<high; j++)
        {
            if(arr[j] < pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }

        i++;
        swap(arr, i, high);

        return i; //pivot index
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        if(arr.length == 0 || low > high)
        {
            return;
        }

        if(low < high)
        {
           int pivotIndex = partition(arr, low, high);
           sort(arr, low, pivotIndex-1);
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
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
