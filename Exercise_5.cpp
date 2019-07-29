#include<iostream>
using namespace std;

// A utility function to swap two elements
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

/* This function is same in both iterative and recursive*/
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

void quickSortIterative(int arr[], int l, int h)
{
    int size = h-l+1;   //to get the size of the stack.
    int stack[size];

    int top = -1;
    stack[++top]=l;		//Push index values to the stack.
    stack[++top]= h;

    while(top>=0) {
        h = stack[top--];
        l = stack[top--];

        int x = partition(arr, l, h);	//set the pivot element for swapping and sorting.

        if (x - 1 > l) {			//push left side elements to the stack
            stack[++top] = l;
            stack[++top] = x - 1;
        }

        if (x + 1 < h) {			//push right side elements to the stack.
            stack[++top] = x + 1;
            stack[++top] = h;
        }


    }

}

// A utility function to print contents of arr
void printArr(int arr[], int n)
{
    int i;
    for (i = 0; i < n; ++i)
        cout << arr[i] << " ";
}

// Driver code
int main()
{
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
    int n = sizeof(arr) / sizeof(*arr);
    quickSortIterative(arr, 0, n - 1);
    printArr(arr, n);
    return 0;
}