// Time Complexity : O(n*n)
// Space Complexity : 0(n) 
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : problem with swap function, it didn't work until I used 2 new variables and applied same logic

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
      int pivot = arr[high]; //Assign last element in arr to be pivot
      int k = low-1;    // this is a pointer to the smaller element
      for(int i=low;i<high;i++){ //iterate through low to high-1
        if(arr[i]<pivot){
          k++;
          swap(arr,k,i);  //if elemet is smaller, then swap
        }
      }
      swap(arr,k+1,high);  //place pivot after all smaller elements
      return k+1;    //return pivot index
    }


    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
             // partition and after partition
      if(low<high) {
        int p = partition(arr, low, high);
        sort(arr, low, p - 1);
        sort(arr, p + 1, high);
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
