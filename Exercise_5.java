class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	/*
    	 * Code for swapping in-place does not work when swapping the same numbers.. have been able to find the cause but not the fix
    	System.out.println("Before: "+arr[i]+" "+arr[j]);
    	arr[i] = arr[i] + arr[j];
    	System.out.println(arr[i] + " " + arr[j]);
    	arr[j] = arr[i] - arr[j];
    	System.out.println(arr[i]+ " "+arr[j]);
    	arr[i] = arr[i] - arr[j];
    	System.out.println(arr[i]+ " "+arr[j]);
    	System.out.println("After: "+arr[i]+" "+arr[j]);
    	*/
    	int temp = arr[i];
    	arr[i] = arr[j];
    	arr[j] = temp;
    	
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	//this method remains same as for quicksort recursive approach
    	int pivot = h;
    	int i = l;
    	for(int j=l;j<h;j++)
    	{
    		if(arr[j]<=arr[pivot])
    		{
    			swap(arr,i,j); 
    			i++;
    		}
    	}
    	swap(arr,i,pivot);
    	return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	int stack[] = new int[h-l+1];//create the stack using array
    	
    	int top = -1; //initializing the stack
    	
    	stack[++top] = l;
    	stack[++top] = h;
    	
    	while(top>=0) //while stack is not empty
    	{
    		//pop initial values off the stack
    		h = stack[top--];
    		l = stack[top--];
    		
    		int pivot = partition(arr,l,h); //partition the array, get the pivot
    		
    		if(pivot-1>l)
    		{
    			stack[++top] = l;
    			stack[++top] = pivot-1;
    		}
    		
    		if(pivot+1<h)
    		{
    			stack[++top] = pivot+1;
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
        //int arr[] = {9,7,3,6};
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 