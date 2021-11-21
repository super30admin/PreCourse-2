//Time Complexity: worst case complexity is O(n ^ 2). average case complexity is O(nlogn) as the array is iterated over for each long recurive calls.
//Space Complexity: Constanct 

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
        int pivot = arr[high]; // as we are considering the last element as pivot
        int i = low -1;
        for(int j = low; j <  high ; j++){ // iterate through the elements in the array and swap every element less than pivot with the i,
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, high); // swap the pivot with element next to i and now all the elements on the left of pivot are smaller than pivot and all elements on the right are bigger than pivot.
        return (i+1);
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
            // partition and after partition
            if(low < high){
                int partition = partition(arr, low, high);
                //after the first partition call sort on the individual partitions.
                sort(arr, low, partition - 1);
                sort(arr, partition +1, high);
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
