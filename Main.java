public class Main {

    public static void main(String args[])
    {
        //Exercise 1
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);

        //Exercise 3
        LinkedList llist = new LinkedList();
        for (int i=15; i>0; --i)
        {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }

        //Exercise 2
        int arr2[] = {10, 7, 8, 9, 1, 5};
        int ne = arr2.length;

        QuickSort obj = new QuickSort();
        obj.sort(arr2, 0, ne-1);

        System.out.println("sorted array");
        obj.printArray(arr2);

        //Exercise 4
        int arr4[] = {12, 11, 13, 5, 6, 7};
        MergeSort msort = new MergeSort();
        System.out.println("Exercise 4: Given Array");
        msort.printArray(arr4);

        msort.sort(arr4);

        System.out.println("\nSorted array");
        msort.printArray(arr4);

        //Exercise 5
        IterativeQuickSort IterativeQuickSort = new IterativeQuickSort();
        int arr5[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        IterativeQuickSort.QuickSort(arr5, 0, arr5.length - 1);
        IterativeQuickSort.printArr(arr5, arr5.length);
    }
}
