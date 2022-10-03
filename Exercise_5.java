
// Time Complexity : O(n2)
// Space Complexity : O(n)

package S30_Codes.PreCourse_2;
import javafx.util.Pair;
import java.util.Arrays;
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    { 
	    //Try swapping without extra variable
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h)
    { 
        int pivot = arr[h];
        int pivotIdx = l-1;

        for(int i=l; i<=h; i++){
            if(arr[i] <= pivot)
                pivotIdx++;
        }

        if(pivotIdx != h)
            swap(arr, pivotIdx, h);

        int part1Idx = l;
        int part2Idx = pivotIdx+1;
        int tempIdx = l;

        while (tempIdx <= h){

            // current element will fall in part 1
            if(arr[tempIdx] <= pivot){

                // current idx is of part 2, so need to move that element in part 1
                if(tempIdx > pivotIdx){
                    while (arr[part1Idx] <= pivot)
                        part1Idx++;

                    swap(arr, tempIdx, part1Idx++);
                }
                tempIdx++;
            }

            // current element will fall in part 2
            else{
                // current index is of part 1, so need to move that element in part 2
                if(tempIdx < pivotIdx){
                    while (arr[part2Idx] > pivot)
                        part2Idx++;

                    swap(arr, tempIdx, part2Idx++);
                }
                tempIdx++;
            }
        }

        return pivotIdx;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        if(l >= h)
            return;

        // stack for storing low, and high Index
        Stack<Pair<Integer, Integer>> stackOfIdx = new Stack<>();
        stackOfIdx.push(new Pair<>(l, h));

        while (!stackOfIdx.empty()) {
            Pair<Integer, Integer> idx = stackOfIdx.pop();
            int low =  idx.getKey();
            int high = idx.getValue();

            int pivotIdx = partition(arr, low, high);

            if(low < pivotIdx-1)
                stackOfIdx.push(new Pair<>(low, pivotIdx - 1));

            if(pivotIdx+1 < high)
                stackOfIdx.push(new Pair<>(pivotIdx + 1, high));
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