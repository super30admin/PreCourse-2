// Time Complexity: O(n^2)
// Space Complexity: O(n)

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        if(arr[i]==arr[j]) {
            return;
        }

        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        // select the last element as pivot
        int pivot = arr[h];
        int pivot_index = l;

        // move all the elements less than pivot to the left of pivot_index
        for(int i=l;i<h;i++) {
            if(arr[i] <= pivot) {
                swap(arr, i, pivot_index);
                pivot_index++;
            }
        }

        // Finally swap the pivot with pivot_index to place the pivot element at the right position
        swap(arr, pivot_index, h);

        return pivot_index;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> st = new Stack<>();

        // we are maintaining the stack to store the low and high indexes for part of the array in execution
        // we push the l and h indexes in the beginning
        st.push(h);
        st.push(l);

        while (!st.isEmpty()) {
            int low = st.pop();
            int high = st.pop();

            int pivot_index = partition(arr, low, high);

            if(pivot_index + 1 < high) {
                st.push(high);
                st.push(pivot_index + 1);
            }

            if(low < pivot_index - 1) {
                st.push(pivot_index - 1);
                st.push(low);
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