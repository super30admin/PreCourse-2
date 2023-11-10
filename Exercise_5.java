import java.util.Stack;

// complexity is O(nlogn) average case and O(n^2) worst case
class IterativeQuickSort { 
    //Gives an error when both the values being swapped are same
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(arr[i] == arr[j]){
            return;
        }
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    // complexity is O(n)
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
        int pivot = arr[high];
        int new_pivot = low-1;
        
        for (int i = low; i <= high-1; i++) {
            
            if (arr[i] <= pivot) {
                
                new_pivot++;
                this.swap(arr, i, new_pivot);
            }
        }
        
        this.swap(arr, new_pivot+1, high);
        
        return new_pivot+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    // complexity is O(log n) avg and O(n) worse case * complexity of partition function
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        // mimicing recursion using stack, splitting low and high with pivot
        Stack<Integer> st = new Stack<Integer>();
        st.push(l);
        st.push(h);

        while(!st.isEmpty()){

            h = st.pop();
            l = st.pop();

            int pivot = this.partition(arr, l, h);
            if(pivot-1 > l){
                st.push(l);
                st.push(pivot-1);
            }

            if(pivot+1 < h){
                st.push(pivot+1);
                st.push(h);
            }
        }
        
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) {
            System.out.print(arr[i] + " "); 
        }
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