import java.util.Stack;

class IterativeQuickSort {


    class Pair {
        private final int x;
        private final int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() { return x; }
        public int getY() { return y; }
    }

    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int a[], int start, int end)
    {
        int pivot = a[end];

        // elements less than the pivot will go to the left of `pIndex`
        // elements more than the pivot will go to the right of `pIndex`
        // equal elements can go either way
        int pIndex = start;

        // each time we find an element less than or equal to the pivot,
        // `pIndex` is incremented, and that element would be placed
        // before the pivot.
        for (int i = start; i < end; i++)
        {
            if (a[i] <= pivot)
            {
                swap(a, i, pIndex);
                pIndex++;
            }
        }

        // swap `pIndex` with pivot
        swap (a, pIndex, end);

        // return `pIndex` (index of the pivot element)
        return pIndex;
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int a[], int start, int end)
    {
        Stack<Pair> stack = new Stack<>();

        // get the starting and ending index of the given array

        // push the start and end index of the array into the stack
        stack.push(new Pair(start, end));

        // loop till stack is empty
        while (!stack.empty())
        {
            // remove top pair from the list and get subarray starting
            // and ending indices
            start = stack.peek().getX();
            end = stack.peek().getY();
            stack.pop();

            // rearrange elements across pivot
            int pivot = partition(a, start, end);

            // push subarray indices containing elements that are
            // less than the current pivot to stack
            if (pivot - 1 > start) {
                stack.push(new Pair(start, pivot - 1));
            }

            // push subarray indices containing elements that are
            // more than the current pivot to stack
            if (pivot + 1 < end) {
                stack.push(new Pair(pivot + 1, end));
            }
        }
        //Try using Stack Data Structure to remove recursion.
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