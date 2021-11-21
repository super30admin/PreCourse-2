class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        int temp= arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];
        int i= low;
        int j = low-1;
        for(i=low;i<high;i++){
           if(arr[i]<pivot){
               j++;
               swap(arr,j,i);
            }
        }
       swap(arr,j+1,high);
       return j+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] mystack = new int[high+1-low];
        int top = -1;

        //push into stack
        top=top+1;
        mystack[top]=low;
        top=top+1;
        mystack[top]=high;

        while(top>=0){
            high=mystack[top];
            // stack pop
            top = top-1;
            low=mystack[top];
            top= top-1;

            int p = partition(arr, low, high);

            if(p-1 > low){
                top=top+1;
                mystack[top]=low;
                top=top+1;
                mystack[top]=p-1;
            }

            if(p+1<high){
                top=top+1;
                mystack[top]= p+1;
                top=top+1;
                mystack[top]= high;
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
        //int arr1[] = { -4, -3, -5, -2, -1, -3, -2, -3}; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length);
        // ob.QuickSort(arr1, 0, arr.length - 1); 
        // ob.printArr(arr1, arr.length); 
    } 
} 