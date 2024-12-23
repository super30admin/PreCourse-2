import java.util.Arrays;

class QuickSort
{
    int pivot =0;
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void swap(int arr[],int i,int j){
        int temp=arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

    }

    int partition(int arr[], int low, int high)
    {
        int temp = 0;
        int i = low;
        int j = high-1;

        pivot = arr[high];

        //Write code here for Partition and Swap

        while (i <= j) {

            if (arr[i] > pivot && arr[j] <= pivot) {
                swap(arr, i, j);
                i++;
                j--;
            } else {
                if (arr[i] <= pivot) {
                    i++;
                }
                if (arr[j] > pivot) {
                    j--;
                }
            }
        }
         swap(arr, i, high);
         System.out.println(Arrays.toString(arr));
         System.out.println(j);
         return i;
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {

        // Recursively sort elements before
        // partition and after partition
            int index=0;

            if (low <high) {
                index=partition(arr, low, high);
               sort(arr, low, index-1);
               sort (arr, index+1, high);
            }



    }


    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }


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
