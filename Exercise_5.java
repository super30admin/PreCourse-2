
class IterativeQuickSort {
    //Time Complexity - O(nlogn)
    //Space Complexity - O(n)
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
        //index to keep track of current position of pivot in sorted array
        int i = l-1;
        for(int j =l; j < h; j++) {
            //if any element
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        //swap the pivot and element at index i
        swap(arr,i+1,h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1];
        int top =-1;

        //Push initial elements to stack
        stack[++top] = l;
        stack[++top] = h;

        //while stack is not empty, keep popping the elements
        while(top >= 0) {
            h = stack[top--];
            l = stack[top--];

            //keep pivot at the right position in array
            int p = partition(arr,l,h);

            //if there are elements before the pivot, push left side onto the stack
            if(p-1 > l) {
                stack[++top] = l;
                stack[++top] = p-1;
            }

            //if there are elements after the pivot, push right side onto the stack
            if(p+1 < h) {
                stack[++top] = p+1;
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