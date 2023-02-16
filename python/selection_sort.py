class SelectionSort:

    def findSmallest(self, vec):

        smallest = vec[0]
        smallest_index = 0

        for i in range(1, len(vec)):

            if vec[i] < smallest:

                smallest = vec[i]
                smallest_index = i

        return smallest_index


    def selectionSort(self, vec):

        new_vec = []
        for i in range(len(vec)):
            
            smallest = self.findSmallest(vec)
            new_vec.append(vec.pop(smallest))

        return new_vec

if __name__ == "__main__":
    
    ss = SelectionSort()
    print(ss.selectionSort([5, 3, 6, 2, 10]))