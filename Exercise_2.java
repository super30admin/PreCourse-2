// Time Complexity : O(NLogN) average case, O(N^2) worst case
// Space Complexity : O(logN), used by recursive calls
// Did this code successfully run on Leetcode : Giving TLE at https://leetcode.com/problems/sort-an-array/description/
// Any problem you faced while coding this : 
// Understanding the pivot algorithm is tricky. Used this resource to understand https://www.youtube.com/watch?v=uXBnyYuwPe8 


// Your code here along with comments explaining your approach



class QuickSort {
    /*
     * This function takes last element as pivot,
     * places the pivot element at its correct
     * position in sorted array, and places all
     * smaller (smaller than pivot) to left of
     * pivot and all greater elements to right
     * of pivot
     */
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) { 
        // i is the position before which all elements less than pivot are present
        // j is a pointer that traverses the array to find an element such that it is less than the pivot
        // If it is, then we swap it with i and increment it

        int i=low;
        int j=low;
        for(;j<high;j++){
            if(arr[j]<arr[high]){
                swap(arr, i, j);
                i++;
            }
        }
        swap(arr,i,high);
        return i;
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        if (low >= high)    return;
        // Recursively sort elements before
        // partition and after partition
        int partInd = partition(arr, low, high);
        sort(arr, low, partInd - 1);
        sort(arr, partInd + 1, high);
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
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
