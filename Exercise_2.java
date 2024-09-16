//TC : Worst Case TC is O(n^2). This happens if the pivot is always the smallest or the largest element of the subarray
//       Average TC is O(nlogn)

//Space Complexity : O(1) if the recursive call stack is not considered
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
        //choose last element as pivot
        int pivot = arr[high];

        //this indicates the most recent smallest element found so far and also the right position of pivot
        int i = low-1;

        for(int j=low; j<=high-1;j++)
        {

            //if the current element is smaller than the pivot, that means it should be moved to the correct index (the index that has the elements smaller than the pivot until now)
            if(arr[j]<pivot)
            {
                i++;
                swap(arr,i,j);
            }

        }

        //at the last swap the pivot with i+1 index element as that is its correct location
        swap(arr,i+1,high);
        return(i+1);

    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
        if (low < high)
        {
            //arr[pi] is now at the right position
            int pi = partition(arr, low, high);

            // Recursively sort elements before
            // partition and after partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
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
