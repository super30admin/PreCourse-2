class
IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable

        if(arr[i]==arr[j]){
            return;
        }
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i]-arr[j];
        arr[i] = arr[i]-arr[j];

    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        int pivot = arr[h];
        int pIndex = l;
        for(int i=l;i<h;i++){
            if(arr[i]<=pivot){
                this.swap(arr,i,pIndex);
                pIndex++;
            }
        }
        this.swap(arr,h,pIndex);
        //Compare elements and swap.
        return pIndex;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.

//         Stack stack = new Stack();
//         stack.push(l);
//         stack.push(h);
//         while(!stack.isEmpty()){

//             int high = (int)stack.pop();
//             int low = (int)stack.pop();
//             int pIndex = this.partition(arr,low,high);
//             if(pIndex-1>low){
//                 stack.push(low);
//                 stack.push(pIndex-1);
//             }
//             if(pIndex+1<h){
//                 stack.push(pIndex+1);
//                 stack.push(high);
//             }

//         }
//         System.out.println(stack.isEmpty());
        int[] stack = new int[h - l + 1];
        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            int high = stack[top--];
            int low = stack[top--];


            int pIndex = partition(arr, low, high);


            if (pIndex - 1 > low) {
                stack[++top] = low;
                stack[++top] = pIndex - 1;
            }


            if (pIndex + 1 < high) {
                stack[++top] = pIndex + 1;
                stack[++top] = high;
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