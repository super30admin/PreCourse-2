// Time complexity: O(nlogn)
// Space complexity: O(logn)

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        if(i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int i = l - 1;

        for (int j = l; j <= h - 1; j++)  {
            if (arr[j] < arr[h]) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return  i + 1;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) {
        // Basic idea:
        // Step 1: Store the pivot for the first partition into the stack
        // Step 2:Then partition the left array until the pivot reaches to 1
        // Step 3:Use the pivot value stored (Step 1) and partition the right array

        Stack stack = new Stack();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            h = (int) stack.pop();
            l = (int) stack.pop();

            int p = partition(arr, l, h);

            if (stack.isEmpty())
                stack.push(p);

            if (p <= 1) {
                l = (int) stack.pop();
                stack.push(l);
                p = arr.length;
            }

            if (p == l) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                stack.push(l);
                stack.push(p - 1);
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