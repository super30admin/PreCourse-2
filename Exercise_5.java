// Time Complexity : O(Nlogn)
// Space Complexity : O(n) as we are using stack of n 
// Did this code successfully run on Leetcode : Not applicable
// Any problem you faced while coding this : calculating time complexity and the problem with swapping without extra variable if both of
// them are referring to the same index.  

// Approach : get the pivot element sorted out such that the elements towards the left of the pivot are less than pivot
// and the elements that are greater than pivot are towards the right of pivot 
// use a stack, push the low and high , pop them and call partition method, if we have left subarray push low and p-1 where p is index returned by partition method.
// if we have right sub array push p+1 and h, while top >0

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(!(i==j))
        {
            arr[i]=arr[i]+arr[j];
            arr[j]=arr[i]-arr[j];
            arr[i]=arr[i]-arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = (l - 1);
        for (int j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];
        int top=-1;
        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {

            h = stack[top--];
            l = stack[top--];

            int p = partition(arr, l, h);
 
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }
            if (p + 1 < h) {
                stack[++top] = p + 1;
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
            System.out.println();
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