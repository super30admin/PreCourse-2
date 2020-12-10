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
        int partition_index = l;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] < pivot){
                swap(arr,i,partition_index);
                partition_index++;
            }
        }
        swap(arr,partition_index,pivot);
        return partition_index;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> left_boundary = new Stack();
        Stack<Integer> right_boundary = new Stack();

        left_boundary.push(l);
        right_boundary.push(h);


        while (!left_boundary.isEmpty() && !right_boundary.isEmpty()){
            int left = left_boundary.pop();
            int right = right_boundary.pop();
            int partition_index = partition(arr,left,right);

            //base condition
            if (left < right) {
                left_boundary.push(left);
                right_boundary.push(partition_index - 1);

                left_boundary.push(partition_index + 1);
                right_boundary.push(right);
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