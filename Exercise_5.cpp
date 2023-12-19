// Time Complexity : O(NlogN)
// LogN as we are divided the array into two halves,
// pivot placement each time for N elements
// Space Complexity : O(N)
// Use of Stack

#include <bits/stdc++.h>
using namespace std;

// A utility function to swap two elements
void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

/* This function is same in both iterative and recursive*/
int partition(int arr[], int low, int high)
{
    // Your Code here
    int pivot = arr[high], start = low - 1, end = low;

    // check till end reach last but one index
    while (end < high)
    {
        // if element is less than equal to pivot,
        // we have to swap the element
        if (arr[end] <= pivot)
        {
            // as start in below low, increment and swap
            start++;

            swap(arr[start], arr[end]);
        }

        end++;
    }

    // once end reaches the last but one index,
    // correct position of pivot is found at start+1
    // swap the pivot with start+1
    start++;

    swap(arr[start], arr[high]);

    // return the pivot index
    return start;
}

/* A[] --> Array to be sorted,
l --> Starting index,
h --> Ending index */
void quickSortIterative(int arr[], int l, int h)
{
    // Try to think that how you can use stack here to remove recursion.
    int partitionIndex;

    stack<int> st;

    // adding start and ending indices to stack
    st.push(l);
    st.push(h);

    int start, end;

    while (!st.empty())
    {
        // get the indices of the array which we have to sort from the stack
        end = st.top();
        st.pop();

        start = st.top();
        st.pop();

        // place the pivot at the right position and get the paritition index
        partitionIndex = partition(arr, start, end);

        // add the first half starting from (start) and ending at (partitionIndex - 1)
        // check if partitionIndex-1 is same as start or not
        if (partitionIndex - 1 > start)
        {
            st.push(start);
            st.push(partitionIndex - 1);
        }

        // add the second half starting from (partitionIndex+1) and ending at (end)
        // check if partitionIndex+1 is same as end or not
        if (partitionIndex + 1 < end)
        {
            st.push(end);
            st.push(partitionIndex + 1);
        }

        // use of stack is same as recursion call stack,
        //  but we are replicating the functionality with extra space
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
    int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
    int n = sizeof(arr) / sizeof(*arr);
    quickSortIterative(arr, 0, n - 1);
    printArr(arr, n);
    return 0;
}