// Slack ID: Prajakta Ganesh Jalisatgi_RN38APR2021
// Exercise_5 : Iterative Quick Sort.
// Time Complexity : O(n*logn) where n is the size of the given array
// Space Complexity : O(n) where n is the size of the given array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Yes, didn't know how to solve this

public class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        arr[i] = (arr[i] + arr[j]) - (arr[j] = arr[i]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = (l - 1); // index of smaller element
        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or
            // equal to pivot
            if (arr[j] <= pivot) {
                i++;
                // swap arr[i] and arr[j]
                swap(arr,i,j);
            }
        }
  
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;
  
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        // Create an auxiliary stack
        int[] s = new int[h - l + 1];
  
        // initialize top of stack
        int top = -1;
  
        // push initial values of l and h to stack
        s[++top] = l;
        s[++top] = h;
  
        // Keep popping from stack while is not empty
        while (top >= 0) {
            // Pop h and l
            h = s[top--];
            l = s[top--];
  
            // Set pivot element at its correct position
            // in sorted array
            int p = partition(arr, l, h);

            // If there are elements on left side of pivot,
            // then push left side to stack
            if (p - 1 > l) {
                s[++top] = l;
                s[++top] = p - 1;
            }
  
            // If there are elements on right side of pivot,
            // then push right side to stack
            if (p + 1 < h) {
                s[++top] = p + 1;
                s[++top] = h;
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
        //1 2 2 3 3 3 4 5 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 