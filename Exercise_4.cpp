
#include<iostream>
using namespace std;

void merge(int arr[], int l, int m, int r)
{
    int temp[50];       //Created a temporary array of size 50 to store the sorted elements after comparing.
    int i = l;          // Index i will start from the left part of divided array/
    int j = m+1;        // Index j will start from Mid+1 index that is the right part of the divided array.
    int k = l;
    // Index k is the starting index of the temporary array created.

    while(i<=m && j<=r) {
        if (arr[i] < arr[j])          //Checks the condition if the element in the left is smaller than the right.
        {
            temp[k] = arr[i];    // IF left smaller , then it is added to the temporary array and indices are incremented.
            k++;
            i++;
        } else {
            temp[k] = arr[j];    // If right is smaller, then right element is added to temp array and indices incremented.
            k++;
            j++;
        }
    }
     //If there are elements still left in the left array and finished in right array
        while(i<=m){
            temp[k]=arr[i];
            k++; i++;
        }

        //If there are still elements left in the right array and finished in left array.
        while(j<=r)
        {
            temp[k]=arr[j];
            k++; j++;
        }



      int size_temp = sizeof(temp)/sizeof(temp[0]);

        for(int i=l;i<=r;i++)            // To store the temporary array back to original array to get the final sorted array.
        {
           arr[i]=temp[i];
        }
}


void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {

        int m = l+(r-l)/2;          // Find the mid point of the array to sort different halves.

        mergeSort(arr, l, m);       // Sort the first half of the array.
        mergeSort(arr, m+1, r);    // Sort the second half of the array.
        merge(arr, l, m, r);         // merge the sorted arrays together.
    }
}


void printArray(int A[], int size)      // Function to the print the array.
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr,arr_size);
    return 0;
}





