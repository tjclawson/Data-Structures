class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # swaps root and last element
        self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
        # delete last element which is now the max
        deleted_value = self.storage.pop()
        # sifts down the new root element to ensure heap property is maintained
        self._sift_down(0)
        return deleted_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.storage[index] > self.storage[parent_index]:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            return self._bubble_up(parent_index)

    def _sift_down(self, index):
        bigger_child = self._get_bigger_child(index)
        if bigger_child is not None and bigger_child > self.storage[index]:
            bigger_child_index = self.storage.index(bigger_child)
            self.storage[bigger_child_index], self.storage[index] = self.storage[index], self.storage[bigger_child_index]
            return self._sift_down(self.storage.index(bigger_child) + 1)

    def _get_bigger_child(self, index):
        right_child = None
        left_child = None
        if (index * 2) + 1 < len(self.storage):
            left_child = self.storage[(index * 2) + 1]
        if (index * 2) + 2 < len(self.storage):
            right_child = self.storage[(index * 2) + 2]
        if right_child is not None and left_child is not None:
            return max(right_child, left_child)
        elif right_child is not None and left_child is None:
            return right_child
        elif right_child is None and left_child is not None:
            return left_child
