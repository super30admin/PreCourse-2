class Exercise_5 { 
    void swap(int arr[], int i, int j) 
    { 
        //swap using a temp variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
         //assign the last element as pivot
       int pivot = arr[h];
  
       //for reference store index of smaller element
       int x = (l - 1);
 
       for (int i = l; i <= h - 1; i++) {
            //check if the current element is smaller than pivot
           if (arr[i] < pivot) {
               //increament smaller index  
               x++;
               swap(arr, x, i);
           }
       }
       swap(arr, x + 1, h);
       return (x + 1); 
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        // create a stack
        int[] stack = new int[h - l + 1];
 
        // initialize top of the stack
        int top = -1;
 
        // push l and h in stack
        stack[++top] = l;
        stack[++top] = h;
 
        // pop elements till stack is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];
 
            // put pivot element at its position
            int p = partition(arr, l, h);
 
            // if there are elements in left side of pivot push them to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }
 
            // if there are elements in right side of pivot push them to stack
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
        Exercise_5 ob = new Exercise_5(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 