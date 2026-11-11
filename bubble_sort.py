array = [7, 8, 8, 7, 9, 7, 3, 5, 2, 7, 8, 3, 4, 2]

for i in range(len(array) - 1):
    array_length = len(array)
    if array[i] > array[i+1]:
        big_num = array[i+1]
        array[i+1] = array[i]
        array[i] = big_num
        print(array)
    if not array_length == 2:
        array_length -= 1
        for i in range(array_length):
            if array[i] > array[i + 1]:
                big_num = array[i + 1]
                array[i + 1] = array[i]
                array[i] = big_num
                print(array)
