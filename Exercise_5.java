import java.util.Stack;

class IterativeQuickSort { 

    class Pair 
    {
        int start;
        int end;

        Pair(int start,int end)
        {
            this.start=start;
            this.end=end;
        }
    }
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(i==j)
        {
            return;
        }
        arr[i]=arr[i]*arr[j];
        arr[j]=arr[i]/arr[j];
        arr[i]=arr[i]/arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pIndex=l;
        for(int i=l;i<h;i++)
        {
            if(arr[i]<arr[h])
            {
                swap(arr, pIndex, i);
                pIndex+=1;
            }
        }   
        swap(arr, h, pIndex);
        return pIndex;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Pair> st = new Stack<>();
        st.push(new Pair(l,h));
        while(!st.isEmpty())
        {
            int start=st.peek().start;
            int end=st.peek().end;
            st.pop();
            int p = partition(arr, start, end);
            if(p-1>start)
            {
                st.push(new Pair(start, p-1));
            }
            if(p+1<end)
            {
                st.push(new Pair(p+1, end));
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