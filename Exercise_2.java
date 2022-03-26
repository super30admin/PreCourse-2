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
        // Time Complexity :  o(1)
        // Space Complexity : 0(1)
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high)
    {
    //Write code here for Partition and Swap
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
        // Time Complexity :  o(1nlog(n))
        // Space Complexity : 0(nlog(n))

        int pivot = arr[high];
        int leftPointer = low;
        int rightPointer = high - 1;

        while (leftPointer < rightPointer) {

            while (arr[leftPointer] <= pivot && leftPointer < rightPointer) {
                leftPointer++;
            }
            while (arr[rightPointer] >= pivot && leftPointer < rightPointer) {
                rightPointer--;
            }
            swap(arr, leftPointer, rightPointer);
        }

        if(arr[leftPointer] > arr[high]) {
            swap(arr, leftPointer, high);
        }
        else {
            leftPointer = high;
        }
        return leftPointer;
    }

    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
            // partition and after partition
        if (low >= high) {
            return;
        }
        int pi = partition(arr, low, high);
        sort(arr, low, pi - 1);
        sort(arr, pi + 1, high);
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        // Time Complexity :  o(n)
        // Space Complexity : 0(n)
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
