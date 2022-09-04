// Time Complexity :
// Space Complexity :91ms
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        // smaller element index
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                // swap the elements
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // swap arr[i+1] and arr[high] (or pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] intStack = new int[h - l + 1];

        int top = -1;

        intStack[++top] = l;
        intStack[++top] = h;

        while (top >= 0) {
            h = intStack[top--];
            l = intStack[top--];

            int pivot = partition(arr, l, h);

            if (pivot - 1 > l) {
                intStack[++top] = l;
                intStack[++top] = pivot - 1;
            }

            if (pivot + 1 < h) {
                intStack[++top] = pivot + 1;
                intStack[++top] = h;
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 