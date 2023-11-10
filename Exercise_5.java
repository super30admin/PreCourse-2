import java.util.*;
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    /* This function is same in both iterative and
       recursive*/
    //Time Complexity=O(n)
    //Space Complexity=O(1)
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int i=l-1;
        int pivot=arr[h];
        for(int j=l;j<=h-1;j++){
            if(arr[j]<pivot){
                //shifting elements less than pivot to the begining of the array
                i++;
                swap(arr,i,j);
            }
        }
        //shifting the pivot to a balanced position->(elements<pivot)(pivot)(elements>pivot)
        swap(arr,i+1,h);
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Because the Stack is not storing Recursive calls in this function,
        //Iterative would be faster than Recursive Quick Sort

        //Time Complexity=T(k)+T(n-k)+n->Wort Case:O(n^2)|Avg case:O(nlogn)
        //Space Complexity=O(1)

        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack=new Stack<>();
        stack.push(l);
        stack.push(h);

        while(!stack.isEmpty()){
            //Popping out to check the length of the array
            int end=stack.pop();
            int start=stack.pop();
            //loop ends if the array size is less than 2
            if(end-start<2){
                continue;
            }
            int p=partition(arr,start,end);

            //pushing the start and end of the 1st sub array
            stack.push(start);
            stack.push(p-1);

            //pushing the start and end of the 2nd sub array
            stack.push(p+1);
            stack.push(end);
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