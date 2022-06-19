// time complexity 0(nlogn)
// space complexity 0(n)

class IterativeQuickSort {

    void swap(int arr[], int i, int j)
    {
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];;
        arr[i]=arr[i]-arr[j];

    }

    /* This function is same in both iterative and
    recursive*/
    int partition(int arr[], int low, int high)
    {
        // in pivot take first element
        int pivot = arr[low];
        // start i from low index
        int i = low;
        // start j from high index
        int j = high;
        // we have to find until index i < index j
        while(i<j) {
            // incr i till arr[i] less than equal to pivot and i is less the high
            while (arr[i] <= pivot && i< high)
            {
                i++;
            }
            // decr j till it is greater than pivot
            while (arr[j] > pivot )
            {
                j--;
            }
            // if i is less than j swap them
            if (i < j)
                swap(arr,i,j);
        }
        // swap pivot with partition position so he gets  his place
        swap(arr,low,j);
        // return partition position
        return j;
    }

    // Sorts arr[l..h] using iterative QuickSort
   void QuickSort(int arr[], int l, int h)
    {
    int stack[]= new int[h-l+1];
    int top =-1;
    stack[++top]=l;
    stack[++top]=h;
        while (top >= 0)
        {
            h=stack[top];
            top--;
            l=stack[top];
            top--;
            int p = partition(arr,l,h);
            if(p - 1 > l)
            {
                stack[++top]=l;
                stack[++top]=p-1;
            }
            if (p + 1 < h) {
                stack[++top] = p + 1;
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
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}