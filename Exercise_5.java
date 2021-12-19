import java.util.Stack;

// Time Complexity : O(n2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Tested successfully on local code editor.
// Any problem you faced while coding this : No

//Approach: Quicksort is based on divide and conquer approach. The array is divided into subarrays based on a pivot element such that elements smaller than pivot
//are on the left of the pivot and element greater than pivot are on its right. This is done repeatedly for the left and right subarrays till a single element is
//left in the array. This is done iteratively using a Stack. A custom class Pair is used that stores the start and end of the subarray. Till the stack is not empty,
// the above process is repeated. In the end, the resulting array we obtain is sorted.
// partition() method returns the pivot index. Inside the partition method, I have taken the rightmost element as the pivot and rearranged the array as mentioned above

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        if(i == j)
            return;
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int p = l-1;
        int i = l;
        int pivot = arr[h];
        while(i < h) {
            if(arr[i] < pivot) {
                p++;
                swap(arr, i, p);
            }
            i++;
        }
        swap(arr, h, p+1);
        return p+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        //Try using Stack Data Structure to remove recursion.
        Stack<Pair> stack = new Stack<>();

        // get the starting and ending index of the given array
        int start = 0;
        int end = arr.length - 1;

        // push the start and end index of the array into the stack
        stack.push(new Pair(start, end));

        // loop till stack is empty
        while (!stack.empty()) {
            // remove top pair from the list and get subarray starting
            // and ending indices
            start = stack.peek().getX();
            end = stack.peek().getY();
            stack.pop();

            // rearrange elements across pivot
            int pivot = partition(arr, start, end);

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

class Pair
{
    private final int x;
    private final int y;

    Pair(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public int getX() { return x; }
    public int getY() { return y; }
}