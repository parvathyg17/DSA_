class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None or self.table[new_index] == "Deleted":
                self.table[new_index] = key
                return True

        return False

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None:
                return False

            if self.table[new_index] == key:
                return True

        return False

    def delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None:
                return False

            if self.table[new_index] == key:
                self.table[new_index] = "Deleted"
                return True

        return False


h = HashTable(10)

h.insert(25)
print(h.table)

h.insert(35)
print(h.table)

h.insert(45)
h.insert(10)
print(h.table)

print(h.search(35))

print(h.delete(35))
print(h.table)