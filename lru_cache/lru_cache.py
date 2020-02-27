import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.list_storage = DoublyLinkedList()
        self.dict_storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dict_storage.keys():
            return_node = self.dict_storage[key]
            self.list_storage.move_to_front(return_node)
            return return_node.value.value


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key not in self.dict_storage.keys():
            if self.list_storage.length == self.limit:
                delete_node = self.list_storage.remove_from_tail()
                del self.dict_storage[delete_node.key]
                self.current -= 1
            self.list_storage.add_to_head(Entry(key, value))
            new_node = self.list_storage.head
            self.dict_storage[key] = new_node
            self.current += 1
        else:
            current_node = self.dict_storage[key]
            self.list_storage.move_to_front(current_node)
            current_node.value.value = value




def print_all_nodes(node):
    while node is not None:
        print(node.value)
        node = node.next


# my_cache = LRUCache(3)
# my_cache.set('item1', 'a')
# my_cache.set('item2', 'b')
# my_cache.set('item3', 'c')
# my_cache.get('item1')
# my_cache.set('item4', 'd')
# print("tities")
# print_all_nodes(my_cache.list_storage.head)
#
# print(my_cache.get('item1'))

