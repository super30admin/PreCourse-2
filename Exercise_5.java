import java.util.ArrayList;
import java.util.List;

// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	int t=arr[i];
	arr[i]=arr[j];
	arr[j]=t;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
	int pivot=arr[l];
   	int i=l+1;
   	int j=h;
   	while(i<j) {
   	    while(i<=h && arr[i]<=pivot) {
   		i++;
   	    }
   	    while(j>=l && arr[j]>=pivot) {
   		j--;
   	    }
   	    if(i<j) {
   		swap(arr,i,j);
   	    }
   	    
   	}
   	swap(arr,l,j);
   	return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) 
    { 
	Stack<List<Integer>> stk=new Stack();
        List<Integer> p=new ArrayList<>();
        p.add(low);
        p.add(high);
        stk.push(p);
        while(!stk.isEmpty()) {
     	   int x=stk.peek().get(0);
     	   int y=stk.peek().get(1);
     	   stk.pop();
     	   int pivot=partition(arr,x,y);
            if(pivot-1>x) {
         	   List<Integer> l1=new ArrayList<>();
         	   l1.add(x);
         	   l1.add(pivot-1);
         	   stk.push(l1);
            }
            if(pivot+1<y) {
         	   List<Integer> l2=new ArrayList<>();
         	   l2.add(pivot+1);
         	   l2.add(y);
         	   stk.push(l2);
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