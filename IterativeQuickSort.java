//TimeComplexity nlog(n)
//SpaceComplexity O(n)

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
	    arr[i] = arr[i] + arr[j];
	    arr[j] = arr[i]-arr[j];
	    arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
	    
	   int pivot = arr[high];
            int pIndex = low;
        
        for(int i = low; i <= high; i++){
            if(arr[i] < arr[pivot]){
                swap(arr,pIndex,i);
            }
        }
        swap(arr,pIndex,pivot);
        return pIndex;
	    
	    
	    
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
	    Stack<Integer> st = new Stack<>();
	    
	    st.push(l);
	    st.push(h);
	    
	    while(!st.isEmpty()){
		    int high = st.pop();
		    int low = st.pop();
		    int p = partition(arr,low,high);
		    if(p-1>1){
			     st.push(low);
		    st.push(p-1);
		    }
		    
		   if(p+1 < h){
			st.push(p+1);
		    st.push(high);   
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
