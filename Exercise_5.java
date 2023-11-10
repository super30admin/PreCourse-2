// Time Complexity :    O(n*n)
// Space Complexity :   O(n)
//  Yes, It's run successfully
// Yes, I faced problem to implement iterative approach of Quicksort , took reference of Internet.

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        arr[i] = arr[j] + (arr[j]=arr[i]) - arr[j]; // swapping logic without extra variable
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot = arr[h]; //assign pivot
        int i = l;
        int j = h;

        //continue iterating this loop till i and j pointer cross each other
        while (i<j){

            while (arr[i]<=pivot && i<h){//when element is smaller than pivot, increment i pointer
                i++;
            }

            while (arr[j]>=pivot && j>l){//when element is larger than pivot, increment i pointer
                j--;
            }

            if (i<j){//check if i and j pointer crossed each other
                swap(arr, i, j);
            }
        }
        swap(arr, i, h); // swap i and pivot
        return i;//return pivot position
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        if(l<h) { //check if low is less than high
            int[] stack = new int[h - l + 1];                       //creating array as stack
            int top = -1;
            stack[++top] = h;                                       //push higher limit
            stack[++top] = l;                                       //puch lower limit

            while (top >= 0) {
                l = stack[top--];                                   //pop lower limit
                h = stack[top--];                                   // pop higher limit

                int partitionElement = partition(arr, l, h);        //get the pivot index

                if (partitionElement - 1 > l) {                     //check if left side of the pivot has more elements and if yes and push new limit into stack
                    stack[++top] = partitionElement - 1;
                    stack[++top] = l;
                }

                if (partitionElement + 1 < h) {                     //check if right side of the pivot has more elements and if yes and push new limit into stack
                    stack[++top] = h;
                    stack[++top] = partitionElement + 1;
                }

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
        //int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        int arr[] = {0};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}