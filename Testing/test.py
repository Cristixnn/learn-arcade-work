# sorting items
my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
print(my_list)

# swap 15 and 14 values
temp = my_list[2]
my_list[2] = my_list[0]
my_list[0] = temp


# 15 57 14 33 72 79 26 56 42 40
# 14 is smallest, swap 14 to position 0
# This is the selection sort. I am selecting the smallest
# and swapping

def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)

# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2
