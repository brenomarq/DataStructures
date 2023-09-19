"""
Bubble Sort
On this file, I was studying ways of implementing a simpe bubble sort algorythm.
There are simpler ways to develop this algorythm, but that was a nice try!
"""
def bubble_sort(elements_list):
    n = 1
    length = len(elements_list)
    comparisons = len(elements_list)

    while n < length:
        i = 1
        while i < comparisons:
            if elements_list[i] < elements_list[i-1]:
                elements_list[i], elements_list[i-1] = elements_list[i-1], elements_list[i]
            i += 1
        comparisons -= 1
        n += 1



int_list = [44, 78, 21, 100, 40, 13]

bubble_sort(int_list)

print(int_list)
