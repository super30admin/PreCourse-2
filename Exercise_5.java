class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        /*
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
         */
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i, j, p;
        p = a[high];
        i = low - 1;
        for(j = low; j < high; j++) {
            if(a[j] < p) {
                i++;
                swap(a, i, j);
            }
        }
        i++;
        swap(a, i, high);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int> s = new Stack<int>();
        s.push(l);
        s.push(h);
        while(!s.empty()) {
            h = s.pop();
            l = s.pop();
            p = partition(a, l, h);

            if(p - 1 > l) {
                s.push(l);
                s.push(p - 1);
            }

            if(p + 1 < h) {
                s.push(p + 1);
                s.push(h);
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