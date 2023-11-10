//Time Complexity: worst case complexity is O(n ^ 2). average case complexity is O(nlogn) as the array is iterated over for each long recurive calls.
//Space Complexity: Order of O(n) as we creating stack to store elements 

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
        int pivot = arr[h];
        int i = l - 1;
        for(int j = l; j < h ; j++){
            if(arr[j] <= pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return (i+1);
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];
        int top = -1;
        stack[++top] =  l;
        stack[++top] = h;
        while(top >= 0){
            h = stack[top--];
            l = stack[top--];
            int partition = partition(arr,l,h);
            if(partition -1 > l){
                stack[++top] = l;
                stack[++top] = partition - 1;
            }
            if(partition+1 < h){
                stack[++top] = partition +1;
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
