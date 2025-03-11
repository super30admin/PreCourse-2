package s30.preCourse2;

/*
* In quicksort, the idea is, the first element becomes the pivot.
* Post this, we try to find the right position of the pivot.
* During this phase, we keep 2 indices. low and high. We increment low and
* decrement high until we find an elements greater than pivot (on low) and
* smaller than pivot (on high) and swap them.
*
* We keep doing this until i<=j. And break the loop.
* */
class QuickSort
{
    /* This function takes first element as pivot,
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
        int pivot = arr[low];
        int i = low;
        int j = high;
        while(i < j) {
            while( i < high && arr[i] <= pivot) {
                i++;
            }
            while( j > low && arr[j] > pivot) {
                j--;
            }
            if( i < j) {
                swap(arr, i, j);
            }
        }
        swap(arr, low, j);
        return j;
    }

    int partition1(int arr[], int low, int high) {
        int i = low + 1;
        int j = high;
        int pivot = arr[low];

        while( i < j ) {
            while(arr[i] < pivot && i < high) {
                i++;
            }
            while(arr[j] > pivot && j > low) {
                j++;
            }
            swap(arr, i, j);
        }
        swap(arr, j , low);
        return j;
    }

    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
        if(low < high) {
            int j = partition(arr, low, high);
            sort(arr, low, j - 1);
            sort(arr, j + 1, high);
        }
    }

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
