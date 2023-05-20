class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    //Time Complexity is o(nlog(n))
     int temp;
     temp  =arr[i];
     arr[i] = arr[j];
     arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i=l;
        for(int j=l;j<h;j++)
        {
            if(arr[j]<=pivot)
            {
                swap(arr,i,j);
                i++;

            }
        }
        swap(arr,i,h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1];
        int top =-1;

        stack[++top] = l;
        stack[++top] = h;

        while(top>=0)
        {
            h = stack[top--];
            l = stack[top--];

            int pi = partition(arr, l, h);
            if(pi-1 >l)
            {
                stack[++top] = l;
                stack[++top] = pi-1;

            }
            if( pi+1 <h)
            {
                stack[++top] = pi+1;
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 ,23,22,1,34,56,6}; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 
