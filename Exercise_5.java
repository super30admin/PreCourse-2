import java.util.Stack;

class IterativeQuickSort {
    void swap(int[] arr, int i, int j)
    { 
	    //Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int low, int high)
    { 
        //Compare elements and swap.
        //Write code here for Partition and Swap
        int pivotIndex = high;

        // Collects all the elements which are smaller than pivot.
        // Keeps track of the Most significant index associated to the smaller element.
        int i = low-1;

        // compare all the elements in the array against pivot
        for(int j = low; j <= pivotIndex-1; j++){

            // If current element is less than pivot throw it back to i.
            if(arr[j] < arr[pivotIndex]){
                i++;
                swap(arr, i, j);
            }
        }

        // once all the elements in the current iteration are organised, swap the pivot element with index next to i.
        // i pointer contains only the elements lesser than pivot.
        swap(arr, i+1, pivotIndex);

        // return the index at which pivot is stored.
        return (i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void quickSort(int[] arr, int l, int h)
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();

        // push the initial array space into stack for sorting.
        stack.push(l);
        stack.push(h);

        // run the sorting on the array until the stack is exhausted.
        while(!stack.isEmpty()){
            // fetch the low and high values of the array space from the stack.
            h = stack.pop();
            l = stack.pop();

            // calculate the pivot index for the above array space.
            int pivot = partition(arr, l, h);

            // If there are elements on the left of the pivot, add them to stack for sorting.
            if(pivot - 1 > l){
                stack.push(l);
                stack.push(pivot-1);
            }

            // If there are elements on the right of the pivot, add them to stack for sorting.
            if(pivot + 1 < h){
                stack.push(pivot+1);
                stack.push(h);
            }
        }
    }
  
    // A utility function to print contents of arr 
    void printArr(int[] arr, int n)
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String[] args)
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.quickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length); 
    }
}