// Time Complexity :0(n^2)
// Space Complexity :O(logn)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :Unable to get the the swap without extra variable working


// Your code here along with comments explaining your approach


class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        /*arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];*/
        int t = arr[i];
        arr[i]=arr[j];
        arr[j]=t;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot = arr[h];
        int lowestIndex = l-1;

        for(int i=l; i<h; i++){
            if(arr[i]<=pivot){
                lowestIndex++;
                swap(arr, lowestIndex, i);
            }
        }

        swap(arr, lowestIndex + 1, h);

        return (lowestIndex + 1);
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        int stack[] = new int[h-l+1];
        int top = -1;

        //adding left and right values to stack
        stack[++top] = l;
        stack[++top] = h;

        while(top>=0){
            //remove values from stack
            h = stack[top--];
            l = stack[top--];

            //set pivot
            int pivot = partition(arr, l, h);

            //push left side of pivot to stack if elements on left side
            if(pivot-1 > l){
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }

            //push right side of pivot to stack if elements on right side
            if(pivot+1 < h){
                stack[++top] = pivot + 1;
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