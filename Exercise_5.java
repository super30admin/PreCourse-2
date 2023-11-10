// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : Couldn't implement on my own. Had to research a little on the internet
 
// A simple pair class in Java
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
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
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
        int compareIndex = l;
        for (int i = l; i < h; i++)
        {
            if (arr[i] <= pivot)
            {
                swap(arr, i, compareIndex);
                compareIndex++;
            }
        }
        swap (arr, compareIndex, l);
        return compareIndex;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Pair> stack = new Stack<>();
 
        // get the starting and ending index of the given array
        int start = l;
        int end = h;
 
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