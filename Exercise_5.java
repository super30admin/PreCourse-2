//Best and Average Case:
//        𝑂(𝑛log𝑛)
//        O(nlogn)
//Worst Case:
//        𝑂(𝑛2)

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        if (i!=j)
        {
            arr[i] =arr[i] +arr[j];
            arr[j] =arr[i] -arr[j];
            arr[i] =arr[i] -arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i=l-1;
        for (int j=l;j<h;j++)
        {
            if (arr[j]<pivot)
            {
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> stack = new Stack<int[]>();
        stack.push(new int[] {l,h});
        while (!stack.empty())
        {
            int[] range = stack.pop();
            int low= range[0];
            int high = range[1];

            /// set pivot element to its correct position in sorted array
            int pivot = partition(arr,low,high);

            // if there are elements on the left side of pivot, push left side to the stack
            if (pivot-1 >low)
            {
                stack.push(new int[] {low, pivot-1});
            }
            // if there are elements on the right side of pivot, push right side to stack
            if (pivot+1 < high)
            {
                stack.push(new int[] {pivot+1, high});
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