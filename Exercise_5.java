// Time Complexity :O(n2)
// Space Complexity :  O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        //arr[i] = arr[i] + arr[j];
        //arr[j] = arr[i] - arr[j];
        //arr[i] = arr[i] - arr[j];

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
        int i = l - 1;  //i+1 will be final location of pivot
        for(int j = l; j < h; j++)
        {
          if(arr[j] < pivot)
          {
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
        //Try using Stack Data Structure to remove recursion.

        int[] stackL = new int[h-l+1];
        int[] stackH = new int[h-l+1];

        int top = 0;

        stackL[top] = l;
        stackH[top] = h;

        while(top >= 0)
        {

          l = stackL[top];
          h = stackH[top];
          top--;

          int p = partition(arr, l, h);

          if(p - 1 > l)
          {
            top++;
            stackL[top] = l;
            stackH[top] = p - 1;
          }

          if(h > p + 1)
          {
            top++;
            stackL[top] = p + 1;
            stackH[top] = h;
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
        ob.printArr(arr, arr.length);
        System.out.println("\nSorted Array:");
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
        System.out.println("\n");
    }
}
