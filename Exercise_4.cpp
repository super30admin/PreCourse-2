#include <iostream>
using namespace std;

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
	int a1 = m - l + 1;
	int a2 = r - m;

	int l_arr[a1],
		r_arr[a2];


	for (int i = 0; i < a1; i++)
		l_arr[i] = arr[l + i];
	for (int j = 0; j < a2; j++)
		r_arr[j] = arr[m + 1 + j];

	int index_a1 = 0,
		index_a2 = 0;
	int merged_index = l;

	while (index_a1 < a1 && index_a2 < a2) {
		if (l_arr[index_a1] <= r_arr[index_a2]) {
			arr[merged_index] = l_arr[index_a1];
			index_a1++;
		}
		else {
			arr[merged_index] = r_arr[index_a2];
			index_a2++;
		}
		merged_index++;
	}

	while (index_a1 < a1) {
		arr[merged_index] = l_arr[index_a1];
		index_a1++;
		merged_index++;
	}

	while (index_a2 < a2) {
		arr[merged_index] = r_arr[index_a2];
		index_a2++;
		merged_index++;
	}
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
	if (l >= r)
		return;

	int mid = l + (r - l) / 2;
	mergeSort(arr, l, mid);
	mergeSort(arr, mid + 1, r);
	merge(arr, l, mid, r);
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
	for (int i = 0; i < size; i++)
		cout << A[i] << " ";
}

/* Driver program to test above functions */
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    cout<<"Given array is \n";
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    cout<<"\nSorted array is \n";
    printArray(arr, arr_size);
    return 0;
}
