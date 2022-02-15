import sorting_algorithms as sa

one = sa.generate_sorted_list(1)
two = sa.generate_sorted_list(1)
print("one: ", one)
print("two: ", two)
# k = sa.merge_sort(one, 0, len(one)-1)
# print(k)

merged = sa.merge_two_ordered_list(one, two)
print(merged)

unsorted_list = sa.generate_unsorted_list(10)
print(unsorted_list)

sorted_list = sa.merge_sort(unsorted_list,0,len(unsorted_list)-1)
print(sorted_list)
