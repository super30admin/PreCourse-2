import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	    //Try swapping without extra variable 
        // a = a + b;
        // b = a - b;
        // a = a - b;
        arr[i] += arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] -= arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i = l;
        while (l<h) {
            if (arr[l] < arr[h]) {
                if (l!=i) swap(arr, l, i);
                i++;
            }
            l++;
        }
        swap(arr, i, h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.

        Stack<Integer> st = new Stack<>();
        st.push(l);
        st.push(h);

        while (!st.isEmpty()) {
            h = st.pop();
            l = st.pop();

            int p = partition(arr, l, h);

            if (p-1 > l) {
                st.push(l);
                st.push(p-1);
            }

            if (p+1 < h) {
                st.push(p+1);
                st.push(h);
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