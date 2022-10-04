// Time Complexity: O(n log n) , considering average case, where n is the length of the array
// Space Complexity: O(n), where n is the size of the array

// Any problem you faced while coding this : swapping logic without third variable

class IterativeQuickSort { 
    void swap(int[] arr, int i, int j) 
    { 
        //if(i<0 || j<0 || i>=arr.Length || j>=arr.Length) return;
	    //Try swapping without extra variable 
        // THIS LOGIC WAS giving the result 1 2 2 3 0 0 4 5 
        //arr[i] = arr[i] + arr[j];
        //arr[j] = arr[i] - arr[j];
        //arr[i] = arr[i] - arr[j]; 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;
        for(int j = l; j<h; j++){
            if(arr[j] < pivot)
                swap(arr, ++i, j);
        }
        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int[] arr, int l, int h) 
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
    void printArr(int[] arr, int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            Console.Write(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String[] args) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.Length - 1); 
        ob.printArr(arr, arr.Length); 
    } 
} 