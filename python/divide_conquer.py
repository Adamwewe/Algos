
def arr_sum(vec: list, acc: int=0):
    if not vec:
        return 0
    return vec[0] + arr_sum(vec[1::])


def count_items(vec: list, n: int=0):
    if not vec:
        return 0
    return 1 + count_items(vec[1::])

def find_max(vec: list, max=0):
    if not vec: 
        return 0 

    if len(vec) == 1:
        return vec[0]

    else:
        max = find_max(vec[1::])
        return vec[0] if vec[0] > max else max
    

x = [2, 10, 12, 4, 6]

print(arr_sum(x))


print(count_items(x))

print(find_max(x))
    