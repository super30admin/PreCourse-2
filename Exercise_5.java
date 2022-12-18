class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
      /* ToDo: This In-place swapping has issue for 2 values! but with extra variable swapping below works correctly
        //Try swapping without extra variable 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
        System.out.println("arr[i]="+arr[i] +" " + "arr[j]="+ arr[j]);
      */
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    {  
        int pivot = arr[high];  // Last element is always Pivot
        int partitionIndex = low; // Initially low index is a partition index

        //Logic to partition array around partition index => Less than <-- Partition Index --> Greater than
        for(int i = low; i < high; i++)
        {
            if(arr[i] <= pivot)
            {
                swap(arr, i, partitionIndex);
                partitionIndex++;
            }
        }
        swap(arr, partitionIndex, high); // At the end, Swap pivot element with the partition index element 

        return partitionIndex;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack stack = new Stack();
        int top = -1;

        //Add initial low and high index into stack
        stack.push(low); top++;
        stack.push(high); top++;

        while(top >= 0)
        {
            high = stack.pop(); top--;
            low = stack.pop(); top--;

            int partitionIndex = partition(arr, low, high);

            //If there are elements at left side of array then add low and high index to stack
            if(partitionIndex - 1 > low)
            {
                stack.push(low); top++;
                stack.push(partitionIndex - 1); top++;
            }

             //If there are elements at right side of array then add low and high index to stack
            if(partitionIndex + 1 < high)
            {
                stack.push(partitionIndex + 1); top++;
                stack.push(high); top++;
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