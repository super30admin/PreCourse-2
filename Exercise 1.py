{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7b68404c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element is present at index 3\n"
     ]
    }
   ],
   "source": [
    "def binary_search(arr, low, high, x):\n",
    "    # Check base case\n",
    "    if high >= low:\n",
    "        mid = (high + low) // 2\n",
    "        # If element is present at the middle itself\n",
    "        if arr[mid] == x:\n",
    "            return mid\n",
    "        \n",
    "        # If element is smaller than mid, then it can only\n",
    "        # be present in left subarray\n",
    "        elif arr[mid] > x:\n",
    "            return binary_search(arr, low, mid - 1, x)\n",
    "        \n",
    "        # Else the element can only be present in right subarray\n",
    "        else:\n",
    "            return binary_search(arr, mid + 1, high, x)\n",
    "        \n",
    "    else:\n",
    "        # Element is not present in the array\n",
    "        return -1\n",
    "    \n",
    "    \n",
    "# Test array\n",
    "arr = [ 2, 3, 4, 10, 40 ]\n",
    "x = 10\n",
    " \n",
    "# Function call\n",
    "result = binary_search(arr, 0, len(arr)-1, x)\n",
    " \n",
    "if result != -1:\n",
    "    print(\"Element is present at index\", str(result))\n",
    "else:\n",
    "    print(\"Element is not present in array\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa82b9f3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
