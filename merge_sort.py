"""
Merge sort
On this file, I was studying ways of implementing a recursive merge sort algorythm.
This algorythm was really fun to develop and debug. 
"""
def merge(left: list[int], right: list[int]):
    new_list = []

    while left and right:
        if left[0] < right[0]:
            new_list.append(left.pop(0))
        else:
            new_list.append(right.pop(0))

    if left:
        new_list.extend(left)
    else:
        new_list.extend(right)

    return new_list


def merge_sort(element: list[int]):
    if len(element) < 2:
        return element

    half = len(element) // 2
    left = merge_sort(element[:half])
    right = merge_sort(element[half:])
    return merge(left, right)



int_list = [44, 78, 21, 100, 40, 13]

print(merge_sort(int_list))
