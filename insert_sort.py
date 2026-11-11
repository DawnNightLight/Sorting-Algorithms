array = [7, 8, 8, 7, 9, 7, 3, 5, 2, 7, 8, 3, 4, 2]

def shift(ary, to_move_pos, target_pos):
    tmp = ary[to_move_pos]
    for i in reversed(range(target_pos, to_move_pos)):
        ary[i + 1] = ary[i]
        print(ary)
    ary[target_pos] = tmp

def sort(ary):
    i = 0
    j = i + 1
    while j < len(ary) and i < len(ary):
        while j < len(ary) and i < len(ary) and ary[j] < ary[i]:
            j += 1
            print(j, ary[j])
            print(i, ary[i])
        while j < len(ary) and i < len(ary) and ary[j] >= ary[i]:
            shift(ary, i, j)
            print('swapped')
            i += 1
            j = 0
            print(ary)






sort(array)