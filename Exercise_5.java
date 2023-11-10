// Time Complexity : O(nlog(n))
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this : yes, how to decide on what to put in while

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
    int partition(int arr[], int low, int high)
    {
        //Compare elements and swap.
            //Write code here for Partition and Swap
            int q=arr[high];
            int i=low-1;
            for(int j=low;j<=high;j++)
            {
                if(q>arr[j])
                {
                    i++;
                    swap(arr, i, j);
                }
            }
            swap(arr,i+1,high);
//        printArr(arr, arr.length);
        return i+1;
    }

    class Obj{
        private final int x;
        private final int y;

        Obj(int x, int y)
        {
            this.x = x;
            this.y = y;
        }

        public int getX() { return x; }
        public int getY() { return y; }
    }

    // Sorts arr[l..h] using iterative QuickSort
    public  void QuickSort(int arr[], int l, int h)
    {
         l =0;
         h = arr.length -1;
        //Try using Stack Data Structure to remove recursion.
        Stack<Obj> s = new Stack<>();
        s.push(new Obj(l,h));
        while (!s.empty())
        {
            int w = s.peek().getX();
            int y = s.peek().getY();
            s.pop();
            int q = partition(arr, w, y);

            if((q-1)>w)
            {
                Obj push = new Obj(l, q-1);
                s.push(push);
            }
            if((q+1)<y)
            {
                Obj push1 = new Obj(q+1, h);
                s.push(push1);
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
        int arr[] = { 4, 3, 6, 9 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}