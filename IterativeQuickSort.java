/*
 * Time complexity: O(n * log n)
 * Space complexity: O(n) // for stack
 */

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];

    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        if(l<0 || h<0) return -1;
        int pivot = l;
        int i = l+1; int j = h;
        while(i < j) {
            while(arr[i] <= arr[pivot] && i < j) 
                i++;
            while(arr[j] > arr[pivot] && i <= j) 
                j--;
            if( i < j) 
                swap(arr, i, j);
        }
        swap(arr, pivot, j);
        return j;

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while(!stack.empty()) {
            int high = stack.pop();
            int low = stack.pop();
            int p = partition(arr, low, high);
            if(p - 1 > low) { 
                stack.push(low);
                stack.push(p - 1);
            }
            if(p + 1 < high) {
                stack.push(p + 1);
                stack.push(high);
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