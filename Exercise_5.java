class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    //ex: arr[i] = 4, arr[j] = 3;
    //after swap: arr[i] =3, arr[j] =4
    if(i == j) return;

    arr[i] = arr[i] + arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        //pick last elemnt as pivot
        int pivot = arr[h];

        //i shows correct position for smaller elemnts
        int i = l-1;

        for(int j = l;j <= h-1; j++){
            if(arr[j] <= pivot){
                i++;
                swap(arr, i, j);
            }
        }
        //put pivot in its correct position 
        swap (arr, i+1, h);

        //return pivot index
        return i+1;


    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //sort(left side)
        //sort right side)

       // but here we use stack instead of recurtion.

      // think of stack like a notebook
      //we write which part of array still needs sorting
       int stack[] = new int [h-l+1];
       int top = -1;

       //push starting and ending index
       stack[++top] = l;
       stack[++top] = h;

       while(top >= 0){
        //pop high and low
        h = stack[top--];
        l = stack[top--];

        //put pivot at corect place
        int p = partition(arr, l, h);
        if(p-1 > l){
            stack[++top] = l;
            stack[++top] =p-1;
        }
        if(p + 1 < h){
            stack[++top] = p+1;
            stack[++top] = h;
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