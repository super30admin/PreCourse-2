import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Write code here for Partition and Swap
        int pivot=arr[l];
        int i=l;
        int j=h;

        while(i<j)
        {
            while( i < arr.length-1 && arr[i]<=pivot){
                i++;
            }
            while(j >0 && arr[j]>pivot){
                j--;
            }
            if(i<j){
                swap(arr,i,j);
            }
        }
        swap(arr, l, j);
        return j;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        int[] stack = new int[h - l + 1];
        int head = -1;
        //Try using Stack Data Structure to remove recursion.


        stack[++head] = l;
        stack[++head] = h;

        while (head >= 0) {
            h = stack[head--];
            l = stack[head--];
            int loc = partition(arr, l, h);
            if (l<loc - 1) {
                stack[++head] = l;
                stack[++head] = loc - 1;
            }
            if (loc + 1 < h) {
                stack[++head] = loc + 1;
                stack[++head] = h;
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