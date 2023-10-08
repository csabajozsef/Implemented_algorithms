import numpy as np
import matplotlib as plt
import random
import time


class NotValidInputType(Exception):
    pass


# timer - inputnak kell fvg amit mér
# kell a típus amin méri
# kell egy fgv ami generálja amin méri
# result pedig egy átlag hossz
# később lehet az input hosszával ábrázolni az average timeot?

def sorting_timer(function_to_time, num_of_runs=10):
    for i in range(num_of_runs):
        templist = generate_unsorted_list()
        start = time.time()
        res = function_to_time(templist)
        end = time.time()
        print(end-start)


def generate_sorted_list(length=100):
    # numpy boolean és arange - speedtest
    result_list = []
    pointer = 0
    while len(result_list) < length:
        temp_truth_value = random.randint(0, 1)
        if temp_truth_value:
            result_list.append(pointer)
        pointer += 1
    return result_list


def generate_unsorted_list(length=100, a=-100, b=100):
    """
    :param length:
    :type length:
    :param a:
    :type a:
    :param b:
    :type b:
    :return:
    :rtype:
    """
    random.seed = 42
    return [random.randint(a, b) for _ in range(length)]


def bubble_sort(list_to_sort):

    length = len(list_to_sort)

    # list length = n
    # last item index = n-1
    # first item index = 0
    # if nothing get swapped in a round, the algorithm is done
    for index_of_rounds in range(length-1):  # n-2 comparison in longest round
        swapped = False
        for index in range(length-1-index_of_rounds):  # index_of_rounds goes from 0..n-2
            # from:  to: n-1 - (n-2) = 1 = [0]
            print("round: ", index_of_rounds)
            print("index_to_check: ", index)
            print("list: ", list_to_sort)
            if list_to_sort[index] > list_to_sort[index+1]:
                list_to_sort[index], list_to_sort[index+1] = list_to_sort[index+1], list_to_sort[index]
                swapped = True
            if not swapped:
                continue  # inner loop has to finish without swapping == all are in correct position
            print(list_to_sort)
        if not swapped:
            break


def merge_two_ordered_list(list_a, list_b):
    pointer_a = 0
    pointer_b = 0
    last_index_a = len(list_a)-1
    last_index_b = len(list_b)-1
    result_list = []

    while pointer_a <= last_index_a and pointer_b <= last_index_b:
        if list_a[pointer_a] <= list_b[pointer_b]:
            result_list.append(list_a[pointer_a])
            pointer_a += 1
        else:
            result_list.append(list_b[pointer_b])
            pointer_b += 1
    # only way to exit the swhile loop is one pointer i out of the list
    # meaning the whole list is in the sorted result == only the other one has elements left
    # the other pointer is already set to the next item in the other list
    if pointer_a > last_index_a:
        result_list.extend(list_b[pointer_b:])
    else:
        result_list.extend(list_a[pointer_a:])

    return result_list


def merge_sort(list_to_sort, index_1, index_2):
    if index_1 == index_2:
        print("returning: ", list_to_sort[index_1])
        return [list_to_sort[index_1]]

    else:

        middle_index = (index_1 + index_2)//2
        print("index1:", index_1, "index2:", index_2, "mid:", middle_index)
        left = merge_sort(list_to_sort, index_1, middle_index)
        right = merge_sort(list_to_sort, middle_index+1, index_2)

        # return right
        return merge_two_ordered_list(left, right)
