/*
T.C O(nlog n)
S.C O(1)
 */

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[l];
        int i = l;
        int j = h;
        System.out.println("Pivot" + pivot + " i:" + i + " j:" + j);
        //{10, 7, 8, 9, 1, 5};
        while(i<j) {
            while (i < j && arr[--j] >= pivot) ;

            if (i < j) {
                arr[i] = arr[j];
            }

            while (i < j && arr[++i] <= pivot) ;
            if (i < j) {
                arr[j] = arr[i];
            }
        }
        arr[j] = pivot;
        return j;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {

            h = stack.pop();
            l = stack.pop();

            int p = partition(arr, l, h);

            if (p > l) {
                stack.push(l);
                stack.push(p);
            }
            if (p + 1 < h) {

                stack.push(p + 1);
                stack.push(h);
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

        int arr[] = { 4, 3, 5, 2, 1 };

        ob.QuickSort(arr, 0, arr.length);
        ob.printArr(arr, arr.length); 
    } 
} 