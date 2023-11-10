import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = h;
        h--;
        while(l <= h){
            //while value at left is less than or equal pivot move low towards right
            if(arr[l] <= arr[pivot]){
                l++;
            }
            //while value at right is greater than pivot move high towards left
            else if(arr[h] > arr[pivot]){
                h--;
            }
            // if both step 1 and step 2 does not match swap left and right
            else{
                swap(arr, l, h);
            }
        }
        //Move pivot to its correct position, if it is not in the correct position
        if (l != pivot)
            swap(arr, l, pivot);
        
        return l;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while(!stack.empty()){
            h = stack.pop();
            l = stack.pop();
            int partition = 0;
            // if lower index is less than high index then perform partition or else skip the iteration
            if(l < h)
                partition = partition(arr, l, h);
            else
                continue;
            //Push lower and higher index of right side to the pivot original position
            stack.push(partition + 1);
            stack.push(h);
            //Push lower and higher index of left side to the pivot original position
            stack.push(l);
            stack.push(partition - 1);
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
        int arr[] = { 1,9,4, 3, 5, 2, 1, 3, 2, 3, 8 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 