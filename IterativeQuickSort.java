

class IterativeQuickSort {
    // Time Complexity :O(nlogn)
// Space Complexity :O(n)
    void swap(int arr[], int i, int j)
    {
//       arr[i]=arr[i]+arr[j];
//        arr[j]=arr[i]-arr[j];
//        arr[i]=arr[i]-arr[j];
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;

        //Try swapping without extra variable
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        int pivot=arr[h];
        int leftPointer=l;
        int rightPointer=h;
        while(leftPointer<rightPointer){
            while (arr[leftPointer]<=pivot && leftPointer<rightPointer) leftPointer++;
            while (arr[rightPointer]>=pivot && leftPointer<rightPointer) rightPointer--;
            swap(arr,leftPointer,rightPointer);
        }
        swap(arr,leftPointer,h);
        return leftPointer;   //Compare elements and swap.
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
         /* For the Iterative QuickSort we will use the stack.
         After partition we will get the leftPointer Index.
         If there are any elements to be sorted on left i.e index-1 we will insert those to the stack.
         And continue to the partition. We will do te same with the right partition.
         */
        int [] stack = new int[h-l+1];
        int top=-1;
        stack[++top]=l;
        stack[++top]=h;
        while(top>=0){
            h=stack[top--];
            l=stack[top--];
            int index=partition(arr,l,h);
            if(index-1>l){
                stack[++top]=l;
                stack[++top]=index-1;
            }
            if(index+1<h){
                stack[++top]=index+1;
                stack[++top]=h;
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}