# On this file, I tried to implement a simple algorythm of quicksort in Python.
# The complexity: best case O(nlogn); worst case O(n^2)
def quick_sort(sequence: list):
    if len(sequence) <= 1:
        return sequence

    pivot = sequence.pop()
    items_lower = []
    items_greater = []
    for item in sequence:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)

    left = quick_sort(items_lower)
    right = quick_sort(items_greater)
    left.append(pivot)
    return left + right


sequence = [20, 30, 10, 60, 50, 90, 80]
print(quick_sort(sequence))
