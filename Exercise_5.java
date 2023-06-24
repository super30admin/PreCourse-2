// Time Complexity : nlog(n) 
// Space Complexity : O(log(n)) - stack space is used to mimic the recursion. It is the height of the recursion stack.
// Did this code successfully run on Leetcode : no, this algorithm fails for large inputs.
// Any problem you faced while coding this : no

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) { 
	    int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) { 
        int i = l, j = h, pivot = arr[l];
        while(i<j){
            while(arr[i] <= pivot && i<h){
                i++;
            }

            while(arr[j] > pivot && j>l){
                j--;
            }

            if(i<j){
                swap(arr, i, j);
            }
        }

        swap(arr, l, j);
        return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int lo, int hi) { 
        Stack<Integer> stack = new Stack<>();
        stack.push(lo);
        stack.push(hi);

        while(!stack.isEmpty()){
             int h = stack.pop();
             int l = stack.pop();

            int pIndex = partition(arr, l, h);

            if(pIndex - 1 > l){
                stack.push(l);
                stack.push(pIndex-1);
            }

            if(pIndex+1 < h){
                stack.push(pIndex+1);
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 