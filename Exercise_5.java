
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

    int partition(int arr[], int l, int h)
    {

        // index of smaller element
        int pivot = arr[h];
        //Compare elements and swap.

        // index of smaller element;
        int i = (l-1);

        for (int j = l; j <= h-1; j++) {
            //if current element is smaller than or
            // equal to pivot

            if(arr[j] <= pivot){
                i++;

                swap (arr,i,j);
            }
        }

        swap (arr,i+1,h);

        return  i+1;

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        //Try using Stack Data Structure to remove recursion.

        //create an stack

        int[] stack = new int[h - l + 1];

        // initialize top of stack

        int top = -1;

        //push the initial values of l and h

        stack[++top] = l;
        stack[++top] = h;

        //keep popping while stack is not empty

        while (top >= 0) {
            //pop h and l;

            h = stack[top--];
            l = stack[top--];

            //set pivot element in correct position and
            // sorted way
            int p = partition (arr, l, h);


            // If there are elements on left side of pivot,
            // then push left side to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }


            // If there are elements on right side of pivot,
            // then push right side to stack
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