// Operation:          Quicksort
// Time Complexity:       n*n
// Space Complexity:       n
// This code gave Time Limit Exceeded error for problem 912 (which is sorting an array) on Leetcode
// No, I didn't face any problem in this problem statement

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
        arr[i] = (arr[j] + (arr[j]=arr[i])) - arr[j] ;
    }

    int partition(int arr[], int low, int high) {
        //Write code here for Partition and Swap
        int i = low;
        int j = high;

        int pivot = arr[high] ;                     // setting up pivot
        while(i<j)
        {
            while(arr[i]<=pivot && i<high)          // leaving values on left hand side(correct side) of pivot
                i++;
            while(arr[j]>=pivot && j>low)           // leaving values on right hand side(correct side) of pivot
                j--;
            if(i<j)
                swap(arr,i,j);
        }
        swap(arr,i,high);                           // swapping pivot to its correct position
        return i;                                   // returning correct index of pivot
    }


//            /* Another Approach */
//            int pivot = high;
//                int flag = 0;
//                    while (flag == 0) {
//                while (arr[pivot] >= arr[i] && pivot != i) {
//                    i++;
//                }
//                if (pivot == i) {
//                    flag = 1;
//                } else if (arr[pivot] < arr[i]) {
//                    swap(arr, pivot, i);
//                    pivot = i;
//                }
//
//                if (flag == 0) {
//                    while (arr[pivot] <= arr[j] && pivot != j) {
//                        j--;
//                    }
//                    if (pivot == j)
//                        flag = 1;
//                    else if (arr[pivot] > arr[j]) {
//                        swap(arr, pivot, j);
//                        pivot = j;
//                    }
//                }
//            }
//                    return i;

    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
        void sort ( int arr[], int low, int high)
        {
            // Recursively sort elements before
            // partition and after partition
            if (low < high) {
                int j = partition(arr, low, high);
                sort(arr, low, j - 1);
                sort(arr, j + 1, high);
            }
        }

        /* A utility function to print array of size n */
        static void printArray ( int arr[])
        {
            int n = arr.length;
            for (int i = 0; i < n; ++i)
                System.out.print(arr[i] + " ");
            System.out.println();
        }
    }

class Exercise_2
{
    // Driver program
    public static void main(String args[])
    {
        //int arr[] = {10, 7, 8, 9, 1, 5};
//        int arr[] = {10, 15, 12, 9, 11, 5};
        int arr[] = {5,1,1,2,0,0};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        QuickSort.printArray(arr);
    }
}
