// Time Complexity : O(Nlog N)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
//1. with partition function, calculate the pivot index as middle index and find right position for it , return the index
//2. will maintain a stack , traverse through until its empty
//3. will pop two elements from stack l and h , once we get index for the pivot from partition func , will push new l and h based and the pivot index

class IterativeQuickSort { 
    //iterative approach- no recursion
    //initialise stack data structure
    Stack<Integer> s = new Stack<Integer>();

    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        s.push(arr[i]);
        arr[i] = arr[j];
        arr[j] = s.pop();
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[(low+high)/2];
         while(low <= high){
             while(arr[low] < pivot){
                 low++;
             }
             while(arr[high] > pivot){
                 high--;
             }
             if(low <= high){
                 swap(arr, low, high);
                 low++;
                 high--;
             }
         }
         return low; 
    } 
  
  int[] newArray(int l,int h){
        int[] e = new int[]{l,h};
        return e;
    }
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> s = new Stack<int[]>();
        int pivot = partition(arr, l, h);
        s.addElement(newArray(pivot+1, h));
        s.addElement(newArray(l, pivot-1));
        int left;
        int right;
        while(s.size() > 0){
            pivot = partition(arr, s.peek()[0], s.peek()[1]);
            left = s.peek()[0];
            right = s.peek()[1];
            s.pop();
            if(pivot+1<right){
                s.push(newArray(pivot+1, right));
            }
            if(left<pivot-1){
                s.push(newArray(left, pivot-1));
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