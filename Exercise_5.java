// Time Complexity : o(nlog(n)) 
// Space Complexity : o(n) 
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
  
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    } 

    
    int partition(int arr[], int l, int h) 
    { 
       
        int pivot = arr[h];
        int curr = l;
        for(int i=l;i<arr.length;i++){
            if(arr[i] < pivot){
                swap(arr,curr,i);
                curr++;
            }
        }
        swap(arr,curr,h);
        return curr ;
    } 

  
    void QuickSort(int arr[], int l, int h) 
    { 
        
        Stack<Integer> stack = new Stack<Integer>();

        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();

            int partition = partition(arr,l,h);      
        if (partition - 1 > l) {
            stack.push(l);
            stack.push(partition - 1);
        }
        if (partition + 1 < h) {
            stack.push(partition + 1);
            stack.push(h);
        }
        }
    } 

    
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
    }