/**
 *  Implements the QuickSort algorithm using a divide-and-conquer approach.
 *  Selects a 'pivot' element, partitions the array into two sub-arrays (less than and greater than the pivot),
 *  and recursively sorts the sub-arrays.
 *  Efficient for large datasets with an average time complexity of O(n log n) and O(n2) in worst case.
 */
class QuickSort
{
    // Method to simply swap two elements of the array
    private void swap(int[] arr, int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    /**
     * Helper method to put last element of array called pivot in its right position
     * @param arr Array to be sorted
     * @param low First index of array
     * @param high Last index of array
     * @return Correct index of the pivot element
     */
    private int partition(int[] arr, int low, int high)
    {
        int i = low - 1;
        int pivot = arr[high];
        // All elements at and before index i are less than pivot
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, ++i, high); // Placing pivot in the right place

        //Returning correct position of pivot
        return i;

    }
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        //Do recursive sorting as long as low < high
        //At low == high, we have single element in the array. It is already sorted
        if (low < high) {
            //This line puts the pivot element in the right place
            int pivotIndex = partition(arr, low, high);

            //This calls sort method on left subarray until array is reduced to single element
            sort(arr, low, pivotIndex - 1);

            //This calls sort method on right subarray
            sort(arr, pivotIndex + 1, high);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length;
        for (int j : arr) System.out.print(j + " ");
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
