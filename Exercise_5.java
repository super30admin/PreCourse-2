import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable   
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int j = l;
        for(int i = l; i < h; i++) {
            if(arr[i] <= pivot) {
                    swap(arr, i, j);
                    j++;
            }
        }
        swap(arr, j, h);
        return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        // use a stack to maintian the low and high values and find partition index 
        // use the partition index as low for the right subarray and as high for left subarray
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            int end = stack.pop();
            int start = stack.pop();

            if (start >= end) 
                continue;

            int pIndex = partition(arr,start,end);
    
            stack.push(pIndex+1);
            stack.push(end);
    
            stack.push(start);
            stack.push(pIndex-1);
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