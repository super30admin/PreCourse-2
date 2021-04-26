
// Time Complexity : O(n2)
// Space Complexity : O(logn)
// Any problem you faced while coding this : //algo diff to understand 

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
  
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;
                //swap
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        //swap
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;
  
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
         int[] stack = new int[h - l + 1];
  
         int top = -1;
   
         // push initial values of l and h to stack
         stack[++top] = l;
         stack[++top] = h;
   
         
         while (top >= 0) { // Keep popping from stack while stack not empty
             h = stack[top--];
             l = stack[top--];
   
             // put pivot element at its appropriate position
             int p = partition(arr, l, h);
   
             // If there are elements on left side of pivot,then push left side to stack
             if (p - 1 > l) {
                 stack[++top] = l;
                 stack[++top] = p - 1;
             }
   
             // If there are elements on right side of pivot,then push right side to stack
             if (p + 1 < h) {
                 stack[++top] = p + 1;
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
        ob.printArr(arr, arr.length); 
        System.out.println("");
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 