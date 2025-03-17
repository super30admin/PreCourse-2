// Time Complexity : O(n^2)
// Space Complexity : O(n)

import java.util.Stack;

class Exercise_5 { 
    void swap(int arr[], int i, int j) 
    {
        if (i==j) {
            return; 
        }
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
        int pivot = arr[h];
        int i = l - 1, j = l;
        while (j < h) {
            if (arr[j] <= pivot)
                swap(arr, ++i, j);
            j++;
        }
        swap(arr, ++i, j);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            int nh = stack.pop();
            int nl = stack.pop();

            if (nl >= nh)
                continue;

            int pivot = partition(arr, nl, nh);

            stack.push(nl);
            stack.push(pivot - 1);

            stack.push(pivot + 1);
            stack.push(nh);
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
        Exercise_5 ob = new Exercise_5(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 