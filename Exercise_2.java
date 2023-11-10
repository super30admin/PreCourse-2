class QuickSort
{
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void quicksort(int arr[],int start,int end){
        //Your code here
        if (start<end){
            int index = Partition(arr,start,end);
            quicksort(arr, start, index-1);
            quicksort(arr, index+1, end);
        }
    }

    int Partition(int arr[], int start, int end){
        int pivot = arr[end];
        int index = start;
        for (int i = start; i<end;i++){
            if(arr[i]<=pivot){
                swap(arr,i,index);
                index++;
            }
        }
        swap(arr, index, end);
        return index;
    }

    void swap(int arr[],int i,int j){
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
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
        ob.quicksort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
