import java.util.Stack;

class IterativeQuickSort {
    int pivot;
    void swap(int arr[], int i, int j)
    {
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];
	//Try swapping without extra variable
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        pivot = arr[h];
        int i=l-1;
        for(int x=l; x <= h -1;x++)
        {
            if(arr[x]<=pivot)
            {
                i++;
                swap(arr,i,x);
            }
        }
        swap(arr,i+1,h);
        return i+1;


        //Compare elements and swap.
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        int top = -1;
        int[] stack = new int[h - l + 1];
        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];
            int set = partition(arr, l, h);
            if (set - 1 > l) {
                stack[++top] = l;
                stack[++top] = set - 1;
            }
            if (set + 1 < l) {
                stack[++top] = set + 1;
                stack[++top] = h;
            }
        }
    }
        //Try using Stack Data Structure to remove recursion.

//        Stack s = new Stack();
//        s.push(0);
//        s.push(h);
//        while(!s.isEmpty())
//        {
//            h=(int)s.pop();
//            l=(int)s.pop();
//            if(h-l<2)
//            {
//                continue;
//            }
//            int set = partition(arr,l,h);
//            s.push(set+1);
//            s.push(h);
//            s.push(l);
//            s.push(set);
//        }
//    }

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