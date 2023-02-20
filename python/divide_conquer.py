
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
    
def binary_search(arr: list, item: int, low=0):
    # TODO: come back to this!
    print("mid: {}".format(low))
    high = len(arr) - 1
    mid = (high + low) // 2
    guess = arr[mid]


    if low <= high:


        print("guess: ", guess)


        if not arr:
            return None 
        
        if guess == item:
            return guess

        if guess > item:
            return binary_search(arr, item, mid -1)
        
        if guess < item:
            return binary_search(arr, item, mid+1)

    elif guess == item:
        return guess

    else:
        return None

def quicksort(arr: list):

    if len(arr) < 2:
        return arr
    
    pivot = arr[0]

    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

    

x = [2, 10, 12, 4, 6]

print(arr_sum(x))


print(count_items(x))

print(find_max(x))


sorted_x = quicksort(x)
print(binary_search(sorted_x, 8))


