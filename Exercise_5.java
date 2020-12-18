
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
        int lastElement = arr[h];
        int sortedIndex = l-1;
         for(int i = l; i < h; i++){
             if(arr[i] < lastElement){
                 sortedIndex++;
                 swap(arr, sortedIndex, i);
             }
         }
        swap(arr, sortedIndex+1, h);
        return sortedIndex+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //What do we need to add to the stack?
        int[] stack = new int[h-l+1];
        int top = -1;
        top += 1;
        stack[top] = l;
        top += 1;
        stack[top] = h;
        while(top >= 0){
            h = stack[top];
            top -= 1;
            l = stack[top];
            top -= 1;

            int partitionIndex= partition(arr,l,h);

            if(partitionIndex-1 > l){
                top += 1;
                stack[top] = l;
                top += 1;
                stack[top] = partitionIndex-1;
            }

            if(partitionIndex + 1 < h){
                top +=1;
                stack[top] = partitionIndex+1;
                top += 1;
                stack[top] = h;
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