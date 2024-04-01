import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    int temp = arr[i]; 
    arr[i] = arr[j]; 
    arr[j] = temp; 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l-1;

        for(int j=l;j<=h-1;j++){
            if(arr[j]<=pivot){
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       Stack<Integer> st = new Stack<Integer>();
        int top = -1;
        top++;st.push(h); 
        top++; st.push(l);

        while(top>=0){
            h = st.pop();top--;
            l = st.pop();top--;
            int p = partition(arr, l,h);
            if(p-1>l){
                top++;st.push(l);
                top++;st.push(p-1);

            }
            if(p+1<h){
                top++;st.push(p+1);
                top++;st.push(h);

            }
        }

    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        System.out.print("Array ------ ");
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.printArr(arr, arr.length); 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 
