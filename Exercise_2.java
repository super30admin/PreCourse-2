// Time Complexity:
// Average Case: O(n log n)
// Worst Case: O(n^2) [when pivot is smallest or largest element every time]
// Best Case: O(n log n) [when pivot divides the array equally]

// Space Complexity:
// O(log n) due to recursion stack (in-place sorting)

class QuickSort 
{ 
    // Utility function to swap two elements
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function takes the last element as pivot,
       places the pivot element at its correct position in the sorted array,
       and places all smaller elements to the left and greater to the right */
    int partition(int arr[], int low, int high) {
        int pivot = arr[high];  
        int i = (low - 1);      

        for (int j = low; j < high; j++) {
            
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        
        swap(arr, i + 1, high);

        return i + 1;
    }

    /* The main function that implements QuickSort */
    void sort(int arr[], int low, int high) {
        if (low < high) {
           
            int pi = partition(arr, low, high);
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[]) {
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
