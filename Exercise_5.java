// Time Complexity : O(nlogn)
// Space Complexity : 0(n)
// Did this code successfully run on Leetcode : Local Environment (IntelliJ)
// Any problem you faced while coding this : had to do some research online for this problem.

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    } 

    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        int small = l-1;

        for(int i=l; i<h; i++ ){
            if(arr[i] <= pivot){
                small++;
                swap(arr,small,i);
            }
        }
        swap(arr, small + 1, h);
        return small + 1;
    } 

    void QuickSort(int arr[], int l, int h) 
    {
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();
            int p = partition(arr, l, h);

            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
            }
        }
    } 

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