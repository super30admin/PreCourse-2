/*
Time Complexity is
Average Case Complexity: O(nlog(n)) -> n for partition and log n for recursive calls
Worst Case Complexity: O(n^2)


Space Complexity:
O(log(n)) =->height pf recursion tree

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
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    int partition(int arr[], int low, int high)
    {
   	//Write code here for Partition and Swap
        int i=low-1;
        int pivot=arr[high];
        for(int j=low;j<high;j++)
        {
            //swap only if elements are less than pivot
            //i will be used to track index of smaller elements
            if(arr[j]<pivot)
            {
                i++;
                swap(arr,i,j);
            }
        }
        //element till it are smaller than pivot
        //so i+1 will be correct position for pivot
        swap(arr,i+1,high);
        //return index of pivot
        return i+1;

    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {

        //
        //breaking condition for sorting
        if(low<high) {
           // this method will return correct index of pivot element
            int index = partition(arr, low, high);
            // Recursively sort elements before pivot
            sort(arr, low, index - 1);
            // partition and after partition
           // Recursively sort elements before pivot
            sort(arr, index + 1, high);
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
