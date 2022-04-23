import java.util.Stack;
// Time Complexity : O(NlogN)
// Space Complexity :O(N) using extra stack for space.
// Did this code successfully run on Leetcode : No, ran it on the editor
// Any problem you faced while coding this : No

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        /* ex.
        6 = 2 + 4
        2 = 6 - 4
        4 = 6-2
        */
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j <= h; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack s = new Stack();
        s.push(l);
        s.push(h);

        while (!s.isEmpty()) {
            int high = (int) s.pop();
            int low = (int) s.pop();

            int p = partition(arr, low, high);
            //if the pivot is greater than l that means we still have more elements on the left of the new pivot index, lets sort that
            if (p-1 > low) {
                s.push(low);
                s.push(p-1);
            }
            if (p+1 < high) {
                //if the pivot is less than h that means we still have more elements on the right of the new pivot index, lets sort that
                s.push(p+1);
                s.push(high);
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
        //int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        int arr[] = {10, 8, 68, 89, 2, 3, 6, 1, 100, 200, 7};
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 