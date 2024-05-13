import java.util.Stack;

/*
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 * */
class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp =arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.

        int pivot = arr[l];
        int i=l, j=h;

        while(i<j){

            //find a higher element in left greater thena pivot;
            while(arr[i] <= pivot && i<h){
                i++;
            }

            //fing element lesser than privot in the right side of the pivot
            while(arr[j] > pivot && j>0) {
                j--;
            }

            if(i<j) swap(arr, i, j);
        }

        swap(arr, l, j);

        return j;

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.

        Stack<Integer> stack = new Stack();

        stack.push(l);
        stack.push(h);


        // if(l<h){

        //     int partition = partition(arr, l, h);

        //     QuickSort(arr, l, partition-1);
        //     QuickSort(arr, partition+1, h);
        // }


        while(!stack.isEmpty() && stack.size() >= 2){

            int high = stack.pop();
            int low  = stack.pop();

            if(low<high) {

                int partition = partition(arr, low, high);

                //sorting space indexs for the left side of the partition
                int leftLow = low, leftHigh = partition-1;

                //sorting space indexs for the right side of the partition
                int rightLow = partition+1, rightHigh = high;

                if(leftLow < leftHigh) {
                    stack.push(leftLow);
                    stack.push(leftHigh);
                }

                if(rightLow < rightHigh) {
                    stack.push(rightLow);
                    stack.push(rightHigh);
                }

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