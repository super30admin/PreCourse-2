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
        //Compare elements and swap.

        // last element to be the pivot
        int pivot = arr[h];


        int low = (l - 1);


        // compare elements from start with pivot element swap if the element is smaller then pivot with index low
        // incremented
        for (int j = l; j <= h-1; j++) {

            if (arr[j] < pivot) {

                low++;
                swap(arr,low,j);
            }

        }

        // swap pivot and element at index low+1
        swap(arr,low+1,h);

        return (low+1);

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        //Declare stack
        int size = arr.length;
        int stack[] = new int[size];


        int top = -1;

        // push h & l values into stack
        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {

            // Remove h & l everytime until top < 0
            h = stack[top--];
            l = stack[top--];

            int pivotElement = partition(arr,l,h);


            // push elements on the left side of pivot to the stack
            if (pivotElement - 1 > l) {

                stack[++top]  = l;
                stack[++top] = pivotElement - 1;

            }

            //push elements on the right side of pivot to the stack
            if (pivotElement + 1 < h) {
                stack[++top]  = pivotElement + 1;
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