import java.util.Stack;

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
        int i = l - 1;    //index to add smaller numbers than pivot
        //traverse arr and swap elements smaller than pivot and put in arr[i]
        for(int j = l; j < h; j++) {
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        //move pilot after moving all the elements smaller to its correct position
        swap(arr, i + 1, h);
        return i + 1;   //return next index to start adding
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //stack for int[] of pairs {low,high}
        Stack<int[]> myStack = new Stack<>();
        //push initial values to stack
        myStack.push(new int[] {l, h});
        //continue until stack is empty
        while(!myStack.isEmpty()) {
            int[] range = myStack.pop();
            int low = range[0];
            int high = range[1];

            if(low < high) {
                //get pviot
                int pivotIndex = partition(arr, low, high);
                //if there any elements on left of pivot then push them
                if(pivotIndex - 1 > low) {
                    myStack.push(new int[] {low, pivotIndex - 1});
                }
                //if elements are present right to pivot then push them
                if(pivotIndex + 1 < h) {
                    myStack.push(new int[] {pivotIndex + 1, high});
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 