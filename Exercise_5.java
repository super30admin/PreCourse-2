//Space complexity-O(N) && Time complexity-O(n*log(n))
//Ran successfully	
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
        
        // Index of smaller element and
        // indicates the right position
        // of pivot found so far
        int i = (l - 1); 
      
        for(int j = l; j <= h - 1; j++)
        {
              
            // If current element is smaller 
            // than the pivot
            if (arr[j] < pivot) 
            {
                  
                // Increment index of 
                // smaller element
                i++; 
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
    	int a[] = new int[h];    	 
    	int top = -1; 
    	  a[++top]=l; 
    	  a[++top]=h; 
    	  while(top >= 0) 
    	  { 
    	    h = a[top--]; 
    	    l = a[top--]; 
    	    int p = partition(arr, l, h); 
    	    if(p-1>l) 
    	    { 
    	      a[++top] = l; 
    	      a[++top] = p - 1; 
    	    } 
    	    if(p+1<h) 
    	    { 
    	      a[++top] = p + 1; 
    	      a[++top] = h; 
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
