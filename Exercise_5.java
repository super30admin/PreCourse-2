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
       
            int pivot=arr[h];
            int j=l-1;
            for(int i=l;i<=h-1;i++){
                if(arr[i]<pivot){
                    j++;
                    swap(arr,j,i);        
            }

            }
            swap(arr, j+1, h);
            return (j+1);
        }
     
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int st[] = new int[h - l + 1];
        int top = -1; 
        st[++top] = l; 
        st[++top] = h; 
  
        while (top >= 0) { 
            h = st[top--]; 
            l = st[top--]; 
   
            int p = partition(arr, l, h); 
            if (p - 1 > l) { 
                st[++top] = l; 
                st[++top] = p - 1; 
            } 


            if (p + 1 < h) { 
                st[++top] = p + 1; 
                st[++top] = h; 
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