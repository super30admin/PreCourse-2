# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
# Well, taking the lowest index as pivot for the partition
# and sort everything through recursion
class QuickSort:
    def __init__(self, array: list):
        self._a = array

    def _partition(self, low, high) -> int:
        (_i, _j) = (low, high)
        _pivot = self._a[low]
        while _i < _j:
            while _i < len(arr) and self._a[_i] <= _pivot:
                _i += 1
            while _j > 0 and self._a[_j] > _pivot:
                _j -= 1
            if _i < _j:
                self._a[_i], self._a[_j] = self._a[_j], self._a[_i]
        self._a[low], self._a[_j] = self._a[_j], self._a[low]
        return _j

    def sort(self, low=None, high=None):
        if low is None and high is None:
            low = 0
            high = len(self._a) - 1
        if low < high:
            j = self._partition(low, high)
            self.sort(low, j - 1)
            self.sort(j + 1, high)
        return self._a


# Driver code to test above
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Sorted array is:")
    print(QuickSort(arr).sort())
