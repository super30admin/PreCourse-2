import java.util.Stack;
   // O(NlogN) average time and O(N^2) worst case time complexity O(N) space
class IterativeQuickSort { 
    void swap(int arr[],int i,int j){  
        //swap values in-place 
        if(i != j) {
            arr[i] = arr[i]+arr[j];
            arr[j] = arr[i]-arr[j];
            arr[i] = arr[i]-arr[j];
        } 
    }
    
    int partition(int arr[], int low, int high) 
    { 
          //Assuming the pivot is the element in index high
          int i = low-1;
          int pivot = arr[high];
          
          //If element at index j is less than pivot, swap j and i index elements
          for(int j = low; j < high; j++) {
              if(arr[j] <= pivot) {
                i++;
                swap(arr,i,j);
              }
          }
          swap(arr,i+1,high);
          return i+1;
    } 



    // Sorts arr[l..h] using iterative QuickSort 
    void quickSort(int arr[], int low, int high) 
    { 
        //Use stack to store low and high values of subarrays
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(low);
        stack.push(high);


        while(!stack.isEmpty()) {
            high = stack.pop();
            low = stack.pop();

            //partition array with pivot
            int partitionIndex = partition(arr,low,high);

            //If there is more than one element in any partition, push its low and high to stack 
            if(low < partitionIndex-1) {
                stack.push(low);
                stack.push(partitionIndex-1);
            }

            if(partitionIndex+1 < high) {
                stack.push(partitionIndex+1);
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
        ob.quickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 