array = [7, 8, 8, 7, 9, 7, 3, 5, 2, 7, 8, 3, 4, 2]
counter = 0

def find_num_rotation():
    global counter
    small_num = array[counter]
    small_num_pos = counter
    for j in range(counter, len(array)):
        if array[j] < small_num:
            small_num = array[j]
            small_num_pos = j
            print(counter, small_num)
    swap_num = array[counter]
    array[small_num_pos] = swap_num
    array[counter] = small_num
    counter += 1
    print(array)

for i in range(len(array)):
    find_num_rotation()


