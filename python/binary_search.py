class BinarySearch:

    def iterative_search(self, vec, item):

        low = 0
        high = len(vec) -1

        while low <= high:
            print(low)
            mid = (low + high) // 2 #floor division to get middle
            guess = vec[mid]

            if guess == item:

                return mid 

            if guess > item:

                low = mid - 1

            else:
                low = mid +1 

        return None


    def recursive_search(self, vec, item, low, mid, high):

        if high >= low:

            mid = (high + low) // 2
            guess = list[mid]

            if guess == item:
                return mid 

            elif guess > item :

                return self.recursive_search(vec, item, low, mid -1, high)
            
            else:

                return self.recursive_search(vec, item, low, mid +1, high)
        else:
            return None  

if __name__ == "__main__":
  # We must initialize the class to use the methods of this class
  bs = BinarySearch()
  my_list = [1, 3, 5, 7, 9]

  
#   print(bs.iteratsive_search(my_list, 3)) # => 1
  print("mok")

  # 'None' means nil in Python. We use to indicate that the item wasn't found.
  print(bs.recursive_search(my_list, -1)) # => None