class Exercise_5 { 
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
        int pivot = arr[h];
        int low = (l -1);
        for(int j = l;j<=h-1;j++){
            if(arr[j]<=pivot){
                low++;
                swap(arr, low,j);
            }
        }
        swap(arr,low+1,h);

        return low+1;

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int [] stackArr = new int[h - l + 1];
        int top=-1;
        stackArr[++top]=l;
        stackArr[++top] =h;

        while(top >=0){
            h = stackArr[top--];
            l = stackArr[top--];

            int p = partition(arr,l,h);


            if(p-1 >l){
                stackArr[++top] = l; 
                stackArr[++top] = p - 1; 
            }
    
            if (p + 1 < h) { 
                stackArr[++top] = p + 1; 
                stackArr[++top] = h; 
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
        Exercise_5  ob = new Exercise_5 (); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 


