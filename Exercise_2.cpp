#include<iostream>
using namespace std;
void swap(int* a, int* b)
{
    int temp;					// Swapping function is defined here.
    temp=*b;
    *b=*a;
    *a=temp;
}


int partition (int arr[], int low, int high)
{
    int pivot = arr[high];			//the pivot point is chosen as the last element in the array.
    int k = (low-1);               //index of smaller element.

    for(int i = low ;i<=high-1;i++)
    {
        if(arr[i]<=pivot)  // comparing element to pivot.
        {
            ++k;                //k value incremented for swapping with current index value.

            swap(&arr[k],&arr[i]);
        }
    }

    swap(&arr[k+1],&arr[high]);         // if high element is the smallest then swap it with the lowest k value.
    return (k+1);                       // return value of k for recursive QuickSort call.

}


void quickSort(int arr[], int low, int high)
{
    if(low<high)
    {
        int k= partition(arr,low,high);         //Function call to partition the array.
        quickSort(arr,low,k-1);                 // recursive call for left side of partition. 
        quickSort(arr,k+1,high);                // recursive call for right side of partition.
    }

}

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver Code
int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}