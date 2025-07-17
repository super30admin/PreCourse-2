import java.util.Stack;

// Time Complexity : O(n^2) - depends on the input
// Space Complexity : O(n) stack memory
// Did this code successfully run on Leetcode : Timit limit exceeds as the leetcode problem looking for o(nlogn)
// Any problem you faced while coding this : Tried with pushing the partition key into the stack instead of the range and had to take help from chatgpt to understand range makes more sense
// Your code here along with comments explaining your approach
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        // swapping will not be needed when i==j
        if(i==j) return;
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
        int initialPointer = l;
        for(int i=l;i<h;i++) {
            if(arr[i]<arr[h]) {
                swap(arr, i, initialPointer);
                initialPointer++;
            }
        }
        swap(arr, h, initialPointer);
        return initialPointer;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Task> stack = new Stack<>();
        Task task = new Task(l, h);
        stack.add(task);
        while(!stack.isEmpty()) {
            Task tasker = stack.pop();
            System.out.println(tasker.l+" "+tasker.h);
            int a = tasker.l;
            int b = tasker.h;
            if(a<b) {
                int c = partition(arr, a, b);
                Task task1 = new Task(a, c - 1);
                Task task2 = new Task(c + 1, b);
                stack.add(task1);
                stack.add(task2);
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
        int arr[] = { -4, 4, 3, 5, 2, -3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}

class Task {
    int l;
    int h;

    public Task(int l, int h) {
        this.l =  l;
        this.h = h;
    }
}