import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        int temp = arr[i] ;
        arr[i] = arr[j];
        arr[j] = temp;

    }
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    {
        int i = low - 1;

        for (int k = low;  k < high ; k++) {

            if (arr[k] < arr[high]) {
                i++;
                swap(arr, i , k);
            }

            printArr(arr, arr.length);
        }


        i = i + 1;
        swap(arr, i , high);

        System.out.println("Printing new array " +  low + " high " +  high);
        printArr(arr, arr.length);

        System.out.print("\n\n");
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        Stack stack= new Stack();


        stack.push(l);
        stack.push(h);

        int i = 0 ;

       for ( ; !stack.isEmpty(); ) {



           if ( ++i == 5)
           {
               break;
           }

           h = (int)stack.pop();
           l = (int) stack.pop();


           int mid = partition(arr, l , h);

           System.out.println("mid : "+mid);


           if (mid - 1 > 1){
               stack.push(l);
               stack.push(mid);

           }


           if (mid + 1 < h) {
               stack.push(mid+1);
               stack.push(h);
           }

           System.out.println(stack.toString());


       }


    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " ");
        System.out.println();
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

/*

Time complexity : O (nlogn)

Space complexity : O (n) for stack


 */
