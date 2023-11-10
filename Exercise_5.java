// Time Complexity : best O(NlogN), worst O(n^2) where array is in desc order
// Space Complexity : O(1) as we only swap the positions
// Did this code successfully run on Leetcode : Ran it locally on IDE and works
// Any problem you faced while coding this : yes, it was little challenging for me
                // iterative solution at first since I had to debug
                // and do multiple trials and error
                // before getting the final iterative solution
                // whereas recursive was easily implemented

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
      //Try swapping without extra variable
      if(i == j) return;
      /*
        To swap without any extra variable, I first added the sum in one of the
        positions and then for second position, subtracted the current value from
        the sum for the current value and in place of the original index subtracted
        the sum and this new value.
      */
      arr[i] += arr[j];
      arr[j] = arr[i] - arr[j];
      arr[i] -= arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        /*
          To partition, I adopted the methodology where in we find the actual
          position for pivot such that all elements to the left irrespective of
          their order for now are smaller than pivot and to the right are larger
        */

        int pivot = high;

        high = low;

        while(high < pivot)
        {
          if(arr[high] <= arr[pivot])
          {
            this.swap(arr, low, high);
            low++;
          }

          high++;
        }

        this.swap(arr, low, high);

        return low;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        if(low >= high) return;

        int partitionIndex = this.partition(arr, low, high);
        /*
          for iterative approach, I used stack where we call the partition in
          similar way as we call the recursion stack so after finding the
          partitionIndex, whatever before it from low should be partitioned
          and similarly to the right till high.
        */
        Stack<Integer> st = new Stack<Integer>();

        st.push(high);
        st.push(low);

        while(!st.isEmpty())
        {
        	low = st.pop();
        	high = st.pop();

        	partitionIndex = this.partition(arr, low, high);

        	if(partitionIndex - 1 > low)
        	{
        		st.push(partitionIndex-1);
            st.push(low);
        	}

        	if(partitionIndex + 1 < high)
        	{
        		st.push(high);
        		st.push(partitionIndex+1);
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
