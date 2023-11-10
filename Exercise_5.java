// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
class Exercise_5 {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
      arr[i] = arr[i] + arr[j];
      arr[j] = arr[i] - arr[j];
      arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int pivot, int l, int h)
    {
        //Compare elements and swap.
        int i=l, j=l;
        while(i<=h)
        {
          if(arr[i] > pivot)
            i++;
          else
          {
            swap(arr, i, j);
            i++;
            j++;
          }
        }
        return j-1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.

        int[] stack = new int[h-l+1];
        int top=-1;


        stack[++top] = l;
        stack[++top] = h;

        while(top>=0)
        {
            h = stack[top--];
            l = stack[top--];

            int pivot = arr[h];
            int pi = partition(arr, pivot, l, h);

            //elements present on the left side of pivot, push left side to stack
            if(l<pi-1)
            {
              stack[++top] = l;
              stack[++top] = pi-1;
            }

            //elements present on the right side of pivot, push right side to stack
            if(h>pi+1)
            {
              stack[++top] = pi+1;
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
        Exercise_5 ob = new Exercise_5();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
