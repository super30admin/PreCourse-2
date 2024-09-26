import java.util.Stack;

class Exercise_5 {
    void swap(int arr[], int i, int j) 
    { 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = l;
        for(int j = l+1; j<h; j++){
            if(arr[j] < pivot){
                swap(arr,i,j);
                i++;
            }
        }
        if(arr[i] > arr[h])
            swap(arr, i, h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();

            int index = partition(arr, l , h);
            if(index - 1 > l){
                stack.push(l);
                stack.push(index - 1);
            }
            if(index + 1 < h){
                stack.push(index+1);
                stack.push(h);
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
        Exercise_5 ob = new Exercise_5();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 