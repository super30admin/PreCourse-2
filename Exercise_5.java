import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
              // 4 ,   6
      arr[i] = arr[i]+arr[j];
      arr[j] = arr[i] - arr[j];
      arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.

      int pivot = arr[l];

     while(l < h) {

       while(l < h && arr[h] >= pivot){
         h--;
       }
        arr[l] = arr[h];

       while(l < h && arr[l] <= pivot){
        l++;
       }

       arr[h] = arr[l];
     }

     arr[l] = pivot;
     return l;
      
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        // Recursively sort elements before
        // partition and after partition
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

      while(!stack.isEmpty()) {
//        System.out.println("here");

        int end = stack.pop();
        int start = stack.pop();

        int mid = partition(arr, start, end);

        if(mid-1 > start) {
          stack.push(l);
          stack.push(mid);
        }

        if(mid+1 < end) {
          stack.push(mid + 1);
          stack.push(h);
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