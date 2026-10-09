class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 

        if(i != j){
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];
        int wall = low;
        for(int i = low; i < high; i++){
            if(pivot > arr[i]){
                swap(arr, i, wall);
                wall++;
            }

        }
        swap(arr, high, wall);
        return wall;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        if(h <= l){
            return;
        }

        int top = -1;
        int [] stackarr = new int[arr.length];

        stackarr[++top] = l;
        stackarr[++top] = h;

        while (top != -1){
            h = stackarr[top--];
            l = stackarr[top--];
            int p = partition(arr, l, h);

            if(l< p-1){
                stackarr[++top] = l;
                stackarr[++top] = p-1;
            }
            if(p+1 < h){
                stackarr[++top] = p+1;
                stackarr[++top] = h;
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

// TC - O(nlogn)
// SC - O(n^2)