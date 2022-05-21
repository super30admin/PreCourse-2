// Time Complexity :O(nlogn)
// Space Complexity :O(n) 
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        return;
    } 
  
    class Range {
        int x;
        int y;
        Range(int X, int Y) {
            x = X;
            y = Y;
        }
        int getX() {
            return x;
        }
        int getY() {
            return y;
        }
    }
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];// making last element the pivot
        int lowpointer = l;// starting a pointer from low
        for (int i = l; i <= h - 1; i++) {
             if (arr[i] <= pivot) {
                swap(arr, lowpointer, i);
                lowpointer++;
            }
        }
        swap(arr, lowpointer, h);
        return lowpointer;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Range> st = new Stack<>();
        st.push(new Range(l, h));
        while (!st.isEmpty()) {
            int x = st.peek().getX();
            int y = st.peek().getY();
            st.pop();
            int pivot = partition(arr, x, y);
            if (x < pivot - 1)
                st.push(new Range(x, pivot - 1));
            if (pivot + 1 < y)
                st.push(new Range(pivot + 1, y));
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
        int arr[] = { 4, 2, 1, 3, 5, 2, 3, 2 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 