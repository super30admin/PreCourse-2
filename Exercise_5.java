import java.util.Stack;

class IterativeQuickSort {

    void swap(int arr[], int i, int j)
    { //eg ar[i]=3 ar[j]=3;
        if(i!=j) {
            arr[i] = arr[i] + arr[j];// 6
            arr[j] = Math.abs( arr[i] - arr[j] );//6-3=3
            arr[i] = Math.abs( arr[i] - arr[j] );//6-3
        }
//        int temp=arr[i];
//        arr[i]=arr[j];
//        arr[j]=temp;
    }


    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        int pivot=arr[h];

        int i=l;
        for(int j=l;j<h;j++){
            if(arr[j]<=pivot){
                swap(arr,i,j);
                i++;

            }
        }
        swap(arr,i,h);
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    //Time complexity is: n(log n) where n is number of elements in an array
    //Space complexity is:o(n)
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack=new Stack<>();
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()){
            h=stack.pop();
            l=stack.pop();
            int partIndex=partition( arr,l,h );
            //this is for left side if(l<h) and parttion(low,partIndex-1)
            if(l<partIndex-1){
                //low
                stack.push(l);
                //high
                stack.push(partIndex-1);

            }
            //this is for right side if(l<h) and parttion(partIndex+1,high)
            if(partIndex+1<h){
                //low
                stack.push(partIndex+1);
                //high
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