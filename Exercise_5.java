import java.util.Stack;
class IterativeQuickSort { 
    int pivot,index,j,i,pindex,top,start,temp, end,last,first,p,lindex;

    void swap(int arr[], int i, int j) 
    { 
      
        
	   arr[i]=arr[i]+arr[j]-(arr[j]=arr[i]);
        
        //Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        pivot=arr[h];
        index=l;
    
         pivot = arr[h];
         index = l ;
  
        for (int j = l; j <h ; j++) {
            if (arr[j] <= pivot) {
                
                swap(arr, j,index );
                index++;
            }
        }
        
        swap(arr, index  , h);
        return index; //Compare elements and swap.
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stk=new Stack<Integer>();
        stk.push(0);
        stk.push(h);

        while(!stk.isEmpty())
        {
            last=stk.pop();
            first=stk.pop();

            p=partition(arr, first,last);
            if(p-1>start){
            stk.push(start);
            stk.push(p-1);
            }
            if(last>p+1){
            stk.push(p+1);
            stk.push(last);
            }
        }

        
        
        //Try using Stack Data Structure to remove recursion.
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