# Python program for implementation of Quicksort


class QuickSortIterative:
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

    def sort(self):
        low = 0
        high = len(self._a) - 1
        size = high - low + 1
        stack = []
        top = 0
        stack.append(low)
        top += 1
        stack.append(high)

        while top >= 0:
            high = stack.pop(top)
            top -= 1
            low = stack.pop(top)
            top -= 1

            p_index = self._partition(low, high)

            if p_index - 1 > low:
                top += 1
                stack.append(low)
                top += 1
                stack.append(p_index - 1)

            if p_index + 1 < high:
                top += 1
                stack.append(p_index + 1)
                top += 1
                stack.append(high)

        return self._a


# Driver code to test above
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Sorted array is:")
    print(QuickSortIterative(arr).sort())
