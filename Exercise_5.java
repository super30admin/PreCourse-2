import java.util.*;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    {
        arr[i] = arr[i] + arr[j];   
        arr[j] = arr[i] - arr[j];   
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        int partitionIdx = l;
        for (int i = l; i < h; i++) {
            if (arr[i] <= pivot) {
                swap(arr, i, partitionIdx);
                partitionIdx++;
            }
        }
        swap(arr, partitionIdx, h);
        return partitionIdx;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        Stack<int[]> stack = new Stack<int[]>();
        stack.push(new int[]{ l, h });
        while (!stack.empty()) {
            int[] pair = stack.pop();
            l = pair[0];
            h = pair[1];
            int partitionIdx = partition(arr, l, h);
            if (partitionIdx + 1 < h) {
                stack.push(new int[] {partitionIdx + 1, h});
            }
            if (partitionIdx - 1 > l) {
                stack.push(new int[] {l, partitionIdx - 1});
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