# Linear Search
# On this file, I was studying how to implement a simple linear search algorythm in python.
def linear_search(key, elements_list):
    for elem in elements_list:
        if elem == key:
            return True
    return False
