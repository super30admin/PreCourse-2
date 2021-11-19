#include <iostream>
using namespace std;

//Time Complexity --> O(Logn)
//Space Complexity --> O(Logn)
int binarySearch(int arr[], int l, int r, int x)
{
    if(l > r) return -1;
    int mid = (l+r)/2;
    if(arr[mid] == x){
        return mid;
    }else if(arr[mid] < x){
        return binarySearch(arr, mid +1,r, x);
    }else if(arr[mid] > x){
        return binarySearch(arr, l,mid-1, x);
    }
    return 0;
}

int main(void)
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d",
                            result);
    return 0;
}