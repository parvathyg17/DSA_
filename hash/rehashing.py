class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size


    # Hash function
    def hash_function(self, key):
        return key % self.size


    # Calculate load factor
    def load_factor(self):
        count = 0

        for value in self.table:
            if value is not None and value != "Deleted":
                count += 1

        return count / self.size


    # Insert
    def insert(self, key):

        index = self.hash_function(key)

        for i in range(self.size):

            new_index = (index + i) % self.size

            if (self.table[new_index] is None or
                    self.table[new_index] == "Deleted"):

                self.table[new_index] = key

                # Check whether rehashing is needed
                if self.load_factor() > 0.7:
                    self.rehash()

                return True

        return False


    # Search
    def search(self, key):

        index = self.hash_function(key)

        for i in range(self.size):

            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                return False

            if self.table[new_index] == key:
                return True

        return False


    # Delete
    def delete(self, key):

        index = self.hash_function(key)

        for i in range(self.size):

            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                return False

            if self.table[new_index] == key:
                self.table[new_index] = "Deleted"
                return True

        return False


    # Rehash
    def rehash(self):

        # Save old table
        old_table = self.table

        # Double table size
        self.size = self.size * 2

        # Create new empty table
        self.table = [None] * self.size

        # Insert old elements again
        for key in old_table:

            if key is not None and key != "Deleted":
                self.insert(key)


# -------------------
# Testing
# -------------------

h = HashTable(5)

h.insert(10)
print(h.table)
print("Load Factor:", h.load_factor())

h.insert(20)
print(h.table)
print("Load Factor:", h.load_factor())

h.insert(30)
print(h.table)
print("Load Factor:", h.load_factor())

h.insert(40)

print("After inserting 40:")
print(h.table)

print("New Size:", h.size)
print("Load Factor:", h.load_factor())

print("Search 30:", h.search(30))

print("Delete 30:", h.delete(30))
print(h.table)