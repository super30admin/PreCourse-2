//Time Complexity =O(nlogn)
//Space Complexity = O(1)
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
        //To check index of smaller element
        int i = (l - 1);
        for(int j = l;j<=h-1;j++){
            //if Current element is smaller than or equal to pivot
            if(arr[j] <= pivot){
                i++;
                //Swap the elements arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        //swap the elements arr[i+1] and high
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;
  
        return i + 1;
        
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       // Create an auxiliary stack
        int[] stack = new int[h - l + 1];
  
        // initialize the top of stack
        int top = -1;
  
        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;
  
        // Keep popping from stack while is not empty to pop h and l
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];
  
            // Set pivot element at its correct position in sorted array
            int pivot = partition(arr, l, h);
  
            // If there are elements on left side of pivot, then push left side to stack
            if (pivot - 1 > l) {
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }
  
            // If there are elements on right side of pivot,then push right side to stack
            if (pivot + 1 < h) {
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