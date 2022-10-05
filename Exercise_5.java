class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    {
        arr[i] = (arr[i] * arr[j])/ (arr[j] = arr[i]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        //ignore pivot
        //lp moves to right until greater than pivot
        int lp=l, rp= h;

        while(lp < rp) {
            while (arr[lp] < pivot && lp < rp) {
                lp++;
            }
            //rp moves to left until smaller than pivot
            while (arr[rp] >= pivot && lp < rp) {
                rp--;
            }
            swap(arr, lp, rp);

        }
        swap(arr,lp,h); // swap pivot with pointer merging point
        return  lp;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] s = new int[h-l+1];
        int top = -1;
        s[++top] = l;
        s[++top] = h;

        while(top >= 0){
            h = s[top--];
            l = s[top--];

            int p = partition(arr, l, h);

            // if we have elements to the right of the pivot
            if(p+1 < h)
            {
                s[++top] = p+1;
                s[++top] = h;
            }

            //if we have elements to the left of the pivot
            if(l <  p-1)
            {
                s[++top] = l;
                s[++top] = p-1;
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