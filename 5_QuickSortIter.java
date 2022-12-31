// Time Complexity : O(nlogn)
// Space Complexity : O(logn)
// Any problem you faced while coding this : swap function if both indexes are equal, indexes and correct order to push on stack


// Your code here along with comments explaining your approach
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        if(i==j)
            return;
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i]-arr[j];
        arr[i] = arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
        int partitionIdx = low;
        int pivot = high;
        for(int i=low;i<high;i++){
            if(arr[i]<arr[pivot]){
                swap(arr,i,partitionIdx);
                partitionIdx++;
            }
        }
        swap(arr,partitionIdx,pivot);
        return partitionIdx;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()){
            int high = stack.pop();
            int low = stack.pop();
            System.out.println(high);
            System.out.println(low);
            int partitionIdx = partition(arr,low,high);
            if(partitionIdx-1>low){
                stack.push(low);
                stack.push(partitionIdx-1);
            }
            if(partitionIdx+1<high){
                stack.push(partitionIdx+1);
                stack.push(high);
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