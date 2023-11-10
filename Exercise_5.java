// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int i = l-1;
        int pivot = arr[h];
        for(int j = l; j<h; j++){
            if(arr[j]<pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr,i+1,h);
        return i+1;

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        int[] st = new int[arr.length];
        int top = -1;
        st[++top] = l;
        st[++top] = h;
        while(top>=0){
            h = st[top--];
            l = st[top--];
            int p = partition(arr, l, h);
            if(p-1>l){
                st[++top] = l;
                st[++top] = p-1;
            }
            if(p+1<h){
                st[++top] = p+1;
                st[++top] = h;
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