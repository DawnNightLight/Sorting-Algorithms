array = [7, 8, 8, 7, 9, 7, 3, 5, 2, 7, 8, 3, 4, 2]

def sort(ary):
    i, j = 0, len(ary) - 1
    letter = 'j'
    while not i == j:
        while letter == 'j' and not i == j:
            if j < len(ary) and i < len(ary) and ary[j] < ary[i] and not i == j:
                tmp = ary[i]
                ary[i] = ary[j]
                ary[j] = tmp
                letter = 'i'
                print('j done', ary)
            elif j < len(ary) and i < len(ary) and not i == j:
                j -= 1
                print('j-1')
            elif not j < len(ary) or not i < len(ary) and not i == j:
                break
        while letter == 'i' and not i == j:
            if j < len(ary) and i < len(ary) and ary[i] > ary[j] and not i == j:
                tmp = ary[j]
                ary[j] = ary[i]
                ary[i] = tmp
                letter = 'j'
                print('i done', ary)
            elif j < len(ary) and i < len(ary) and not i == j:
                i += 1
                print('i+1')
            elif not j < len(ary) or not i < len(ary) and not i == j:
                break
    if i == j and len(ary) > 2:
        print('the ary is:', ary)
        left = ary[:i]
        right = ary[i + 1:]
        tmp = ary[i]
        if not len(left) < 2:
            left = sort(left)
        print('left done', left)
        if not len(right) < 2:
            right = sort(right)
        print('right done', right)
        final = left
        final.append(tmp)
        final.extend(right)
        print('the end', final)
        return final
    elif i == j and len(ary) <= 2:
        return ary
#2, 4, 3, 7, 8, 7, 8, 9, 8, 7, 5, 3, 2, 7




def quicksort(ary):
    final = sort(ary)
    return final

print('done', quicksort(array))