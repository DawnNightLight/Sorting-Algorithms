array = [7 ,8 ,8 ,7 ,9 ,7 ,3 ,5 ,2, 7,8 , 3 ,4 ,2]
#array = [3, 7, 7, 7, 8, 8, 9, 2, 2, 3, 4, 5, 7, 8]
arrays = []

def split(array):
    split_num = int((len(array)) / 2)
    left = array[:split_num]
    right = array[split_num:]
    return left, right


def join(array1, array2):
    joined_array = []
    j = 0
    i = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            joined_array.append(array1[i])
            print('array1 smaller than 2', joined_array)
            i += 1
        elif array2[j] < array1[i]:
            joined_array.append(array2[j])
            print('array2 smaller than 1', joined_array)
            j += 1
        elif array1[i] == array2[j]:
            joined_array.append(array2[j])
            joined_array.append(array1[i])
            print(joined_array)
            j += 1
            i += 1
    if i >= len(array1) and j < len(array2):
        joined_array.extend(array2[j:])
        print(joined_array)
    elif i < len(array1) and j >= len(array2):
        joined_array.extend(array1[i:])
        print(joined_array)
    print("returned", joined_array)
    return joined_array


def merge_sort(ary):
    if len(ary) == 1:
        return ary
    else:
        left, right = split(ary)
        left = merge_sort(left)
        right = merge_sort(right)
        return join(left, right)

print('last array', merge_sort(array))