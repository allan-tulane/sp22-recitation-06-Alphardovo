import random, time
import tabulate
import sys
sys.setrecursionlimit(100000)

def qsort(a, pivot_fn):
    if len(a) == 0:
        return []
    pivot = pivot_fn(a)
    idx = a.index(pivot)
    a[idx], a[0] = a[0], a[idx]
    i = 0
    j = len(a) - 1
    pivot = a[0]
    while i < j:
        while i < j and a[j] >= pivot:
            j -= 1
        if i < j and a[j] < pivot:
            a[i] = a[j]
        while i < j and a[i] < pivot:
            i += 1
        if i < j and a[i] >= pivot:
            a[j] = a[i]
    lef = qsort(a[:i], pivot_fn)
    mid = [pivot]
    rig = qsort(a[i + 1:], pivot_fn)
    return lef + mid + rig


def sSort(a):
    for i in range(len(a)-1):
        index_of_min = 0
        for j in range(i, len(a)):
            if a[j] < a[index_of_min]:
                index_of_min = j
        a[i], a[index_of_min] = a[index_of_min], a[i]
    return a


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###


def compare_sort(sizes=[10, 20, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda x: qsort(x, lambda y: y[0])
    qsort_random_pivot = lambda x: qsort(x, lambda y: random.choice(y))
    pythonSort = sorted
    # tim_sort = #
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist.copy()),
            time_search(qsort_random_pivot, mylist.copy()),
            time_search(pythonSort, mylist.copy()),
            time_search(sSort, mylist.copy())
        ])
    return result
    ###


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'python sort', 'selection sort'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_print():
    print_results(compare_sort())

#
# random.seed()
# test_print()