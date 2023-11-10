import java.util.Stack;
/*Time complexity
O(nlogn)
*/

/*Space complexity
O(n) as we are maintaining a stack to store low and high markers for each function call
*/

// Did this code successfully run on Leetcode : yes

// Any problem you faced while coding this : none as concepts were already clear while doing recursive quicksort
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 

        if(i==j){
            return;
        }
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot=arr[h];
        int i=l;
        int j=h;

        while(i<j)
        {
            while(arr[i]<pivot && i<h){
                i++;
            }

            while(arr[j]>=pivot && j>l){
                j--;
            }

            if(i<j)
                swap(arr,i,j);
        }

        swap(arr,i,h);
        return i;

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty())
        {
            h=stack.pop();
            l=stack.pop();

            int sortedIndex=partition(arr,  l,  h);

            if(sortedIndex-1>l)
                {
                    stack.push(l);
                    stack.push(sortedIndex-1);
                }
            if(sortedIndex+1<h){
                stack.push(sortedIndex+1);
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
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 