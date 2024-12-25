// Time Complexity : Best Case:- O(nlogn),  Worst Case:- O(n²)
// Space Complexity : O(logn)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int leftIndex = l;
        int rightIndex = h;
        while(leftIndex < rightIndex) {
            while(arr[leftIndex] <= arr[h] && leftIndex < rightIndex) {
                leftIndex++;
            }
            while(arr[rightIndex] >= arr[h] && rightIndex > leftIndex) {
                rightIndex--;
            }
            swap(arr, leftIndex, rightIndex);
        }
        swap(arr, leftIndex, h);
        return leftIndex;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        int[] stackArr = new int[h - l + 1];
        int top = -1;
        stackArr[++top] = l;
        stackArr[++top] = h;

        while (top >= 0) {
            h = stackArr[top--];
            l = stackArr[top--];

            int p = partition(arr, l, h);

            if (p - 1 > l) {
                stackArr[++top] = l;
                stackArr[++top] = p - 1;
            }

            if (p + 1 < h) {
                stackArr[++top] = p + 1;
                stackArr[++top] = h;
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