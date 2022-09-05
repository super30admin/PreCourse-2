class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
        if(i==j) return;

        arr[i]+=arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]-=arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int p=arr[h];
        int small=l-1;
        for(int i=l;i<h;i++)
        {
            if(arr[i]<=p)
            {
                small++;
                swap(arr,small,i);
            }
        }

        swap(arr,small+1,h);
        return small+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        if(l-h==0) return;
    int[] stack = new int[h - l + 1];
 
        int m = 0;
 
        // push initial values of l and h to stack
        stack[m] = l;
        m++;
        stack[m] = h;
 
        // Keep popping from stack while is not empty
        while (m >= 0) {
            // Pop h and l
            h = stack[m];
            m--;
            l = stack[m];
            m--;

            int p = partition(arr, l, h);
            
            if (p - 1 > l) {
                m++;
                stack[m] = l;
                m++;
                stack[m] = p - 1;
            }
 
            // If there are elements on right side of pivot,
            // then push right side to stack
            if (p + 1 < h) {
                m++;
                stack[m] = p + 1;
                m++;
                stack[m] = h;
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
        int arr[] = { 4, 3, 5, 2, -11, -3, 2, -3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 