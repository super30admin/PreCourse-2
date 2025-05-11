// Time Complexity : BC: O(n log n) -> pivot divides exactly into two equal halves
//                   WC: O(n^2) -> when pivote is always smallest or largest
// Space Complexity : BC: O(log n) -> stack grows to log n depth for balanced partitions
//                    WC: O(n) -> stack grows up to n depth in unbalanced partitions
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Spent time reviewing and revising concept
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if(i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = l - 1;

        for(int j=l; j<h; j++) {
            if(arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        int[] stack = new int[h - l +1];

        int top = -1;

        stack[++top] = l; // push initial bounds to stack
        stack[++top] = h;

        while(top >= 0) { //pop from stack until empty
            h = stack[top--]; //pop high and low
            l = stack[top--];

            int p = partition(arr, l ,h);

            if(p-1 > l){    //if there are elements on left of pivot -> push left side
                stack[++top] = l;
                stack[++top] = p-1;
            }

            if(p+1 < h){    //if there are elements on right of pivot -> push right side
                stack[++top] = p+1;
                stack[++top] = h;
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