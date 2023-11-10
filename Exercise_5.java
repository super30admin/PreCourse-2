class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	// //Try swapping without extra variable
        
    if (arr[i] == arr[j]) //  if same return
    return;
        arr[i]=arr[i]*arr[j]; // multiply both the values and store it into i
        arr[j]=arr[i]/arr[j]; // swap value of j by dividing the above i with j 
        arr[i]=arr[i]/arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i=l-1;
        int pivot= arr[h];
        for(int j=l;j<=h-1;j++)
        {
            if(arr[j]<=pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1]; // initialise a stack

        int top=-1; // initialise the top value of the stack

        stack[++top]= l; //store low value into the stack
        stack[++top] = h; // store high value into the stack

        while(top>=0)
        {
            h=stack[top--];  // pop last element i.e high from the stack and store it into h
            l=stack[top--]; // pop first element i.e low from the stack and store it into l

        int p=partition(arr, l, h); //partition using the above h and l values

        if(p-1>l)
        // if p is greater than the stack, then we need to partition the left side 
        {
            //so we store values in to the stack such that to partition between l to p-1
            stack[++top]=l; 
            stack[++top]=p-1;
        }
        
        if (p + 1 < h) {
            //so we store values in to the stack such that to partition between p+1 to h
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
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 