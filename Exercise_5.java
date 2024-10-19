// Avg Time Complexity : o(nlogn)
// space Complexity : o(n) # extra stack memory
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if (i != j) {
            arr[i] = arr[i]+arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i]- arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = low-1;

        for (int j=0;j<=h-1;j++){
            if(arr[j]<pivot){
                i++;
                this.swap(arr,i,j);
            }
        }
        this.swap(arr,i+1,h);
        return i+1
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1];

        // intialize top of the stack 
        int top=-1;

        // push initial values to stack
        stack[++top]=l;
        stack[++top]=h;

        // keep popping the elements from stack until it is not empty
        while(top>=0){
            // pop elements from stack
            l=stack[top--];
            h=stack[top--];

            // Set pivot element at its correct position
            // in sorted array
            int p = this.partition(arr,l,h);

            // now check if there are elements before pivot
            // then push left side to stack
            if (p-1>l){
                stack[++top]=l;
                stack[++top]=p-1;
            }
            // if there are elements on right side of pivot
            // then push right side to stack
            if (p+1<h){
                stack[++top]=p+1;
                stack[++top]=h;
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