class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
        int i = low-1;
        int pivot = arr[high];
        for(int j = low; j < high; j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, high);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1]; // we implement stack as an array
       // Stack<LinkdeList> stack = new Stack<>();

       // initialize the stack
        int top= -1;
        stack[++top] = l;
        stack[++top] = h;

        while(top >= 0){// we do until stack is not empty
            h = stack[top--];
            l = stack[top--];
            // we find partition index
            int p = partition(arr, l, h);

            //we push left side to the stack
            if(p-1 > l){
                stack[++top] = l;
                stack[++top] = p-1;
            }
            //we push right side to the stack
            if(p+1 < h){
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