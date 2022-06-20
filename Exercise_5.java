// Time Complexity : o(nlog(n)) for average case. o(n) for best case if array is already sorted. worst case is o(n^2) if the array is sorted in revesre order
// Space Complexity : o(n) to store the n elements in an array & stack
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
// maintain stack with left index and right index. Pop from the stack and based on the partition index push back to the stack. Partition logic is same as recursive approch so sorting will be done during that.
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int curr = l;
        for(int i=l;i<arr.length;i++){
            if(arr[i] < pivot){
                swap(arr,curr,i);
                curr++;
            }
        }
        swap(arr,curr,h);
        return curr ;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();
            
            int partition = partition(arr,l,h);      
        if (partition - 1 > l) {
            stack.push(l);
            stack.push(partition - 1);
        }
        if (partition + 1 < h) {
            stack.push(partition + 1);
            stack.push(h);
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
