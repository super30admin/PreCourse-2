//Time complexity is O(nlogn)
//Space complexity is O(logn)
//In leetcode timelimit exceeded with this approach.
import java.util.Stack;
public class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
	    int temp = arr[i];
	    arr[i]=arr[j];
	    arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i = l-1;
        int pivot = arr[h];
        for(int j=l;j<=h;j++){
            if(arr[j]<pivot){
                i=i+1;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> st = new Stack<Integer>();
        st.push(l);
        st.push(h);
        while(!st.isEmpty()){
            int end = st.pop();
            int start = st.pop();
            if((end-start)<2)
                continue;
            int p = partition(arr, start, end);
            st.push(start);
            st.push(p-1);
            st.push(p+1);
            st.push(end);
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