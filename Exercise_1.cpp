#include <stdio.h> 

// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x)
{
    int mid = (l + r) / 2;
    if (l > r)
        return -1;
    else if (arr[mid] == x)
        return mid;
    else if (x < arr[mid])
        binarySearch(arr, l, mid - 1, x);
    else
        binarySearch(arr, mid + 1, r, x);

   /* while (l <= r) {
        int mid = (l + r) / 2;
        if (arr[mid] == x)
            return mid;
        else if (x < arr[mid])
            r = mid - 1;
        else
            l = mid + 1;
    }
    return -1;*/
}

int main(void)
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int arr1[] = { -2, 5, 24, 70, 0 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    for (int i = 0;i < n;i++) {
        int result = binarySearch(arr, 0, n - 1, arr[i]);
        (result == -1) ? printf("Element is not present in array")
            : printf("Element is present at index %d",
                result);
    }
    return 0;
}