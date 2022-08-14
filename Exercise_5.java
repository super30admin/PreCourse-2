import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        if(i != j){
            //Try swapping without extra variable
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }

    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //This partition helps in placing the element in the correct location(linear time)
        int pivot = arr[h];
        int leftIndx = l - 1;

        for(int i = l; i <= h - 1; i++){
            if(arr[i] <= pivot){
                swap(arr, ++leftIndx, i);
            }
        }
        swap(arr, ++leftIndx, h);
        return leftIndx;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        int[] stack = new int[h-l+1];

        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while(top >= 0){
            h = stack[top--];
            l = stack[top--];

            int pIndx = partition(arr, l, h);

            if(pIndx - 1 > l){
                stack[++top] = l;
                stack[++top] = pIndx - 1;
            }

            if(pIndx + 1 < h){
                stack[++top] = pIndx + 1;
                stack[++top] = h;
            }
        }


        //Try using Stack Data Structure to remove recursion.
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
        int arr[] = { 3, 2, 1 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 