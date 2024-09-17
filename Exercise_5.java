
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if(i!=j)
        {    arr[i] = arr[i] + arr[j];
             arr[j] = arr[i] - arr[j];
             arr[i] = arr[i] - arr[j];
        }
        
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
       int pivot = arr[high];
       int i = low-1;
       for(int j=low;j<= high -1; j++)
       {
           if(arr[j]<pivot)
           {
               i=i+1;
               swap(arr,i,j);

           }
       } 
       swap(arr,i+1,high);
       //printArray(arr);
       return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1];
        //top = -1
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;
        while(top >= 0)
        {//pop h and l
            h = stack[top--];
            l = stack[top--];
            //printArray(stack);
            int p = partition(arr,l,h);
            System.out.println("\np="+p);
            if(p-1>l)
            {
                stack[++top] = l;
                stack[++top] = p-1;
            }
            if(p+1<h)
            {
                stack[++top] = p+1;
                stack[++top] = h;
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArray(int arr[]) 
    {   int n = arr.length;
        int i;
        System.out.println("\n");
        for (i = 0; i < n; ++i)
    
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 10,9,8,7,6,5,4,3}; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArray(arr); 
    } 
} 