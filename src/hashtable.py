# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        h = 5381
        for c in key:
            c = ord(c)
            h = ((h << 5) + h) + c
        return h

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        # return self._hash(key)  % self.capacity
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        """
        if self.storage[self._hash_mod(key)] is None:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
        elif self._retrieve(key) is not None:
            self._retrieve(key).value = value
        else:
            lp = self.storage[self._hash_mod(key)]
            while lp.next is not None:
                lp = lp.next
            lp.next = LinkedPair(key, value)
        s = set(self.storage)
        if ((len(s) - 1) / self.capacity) > 0.7:
            self.resize()

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        s = self._hash_mod(key)
        lp = self.storage[s]
        if lp.key == key:
            self.storage[s] = lp.next
            return
        elif lp is not None:
            while lp.key != key:
                try:
                    if lp.next.key == key:
                        lp.next = lp.next.next
                except:
                    lp = lp.next
                else:
                    return
        else:
            return
        if ((len(s) - 1) / self.capacity) < 0.2:
            self.capacity = self.capacity / 4
            self.resize()

    def _retrieve(self, key):
        s = self._hash_mod(key)
        lp = self.storage[s]
        if lp is not None:
            while lp.key != key:
                if lp.next is not None:
                    lp = lp.next
                else:
                    return None
            return lp

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        lp = self._retrieve(key)
        try:
            return lp.value
        except:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity
        for i in old_storage:
            if i is not None:
                lp = i
                while hasattr(lp, "key"):
                    self.insert(lp.key, lp.value)
                    if lp.next is not None:
                        lp = lp.next
                    else:
                        break


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
