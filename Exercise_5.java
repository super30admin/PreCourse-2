// Time Complexity : O(NlogN)
// Space Complexity : O(N)
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int Index = l;
        for(int i=l;i<h;i++){
            if(arr[i]<=pivot){
                this.swap(arr,i,Index);
                Index++;
            }
        }
        this.swap(arr,h,Index);
        return Index;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];
        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            int high = stack[top--];
            int low = stack[top--];


            int Index = partition(arr, low, high);


            if (Index - 1 > low) {
                stack[++top] = low;
                stack[++top] = Index - 1;
            }


            if (Index + 1 < high) {
                stack[++top] = Index + 1;
                stack[++top] = high;
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