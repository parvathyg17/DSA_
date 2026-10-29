class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)

        for value in self.table[index]:
            if value == key:
                return True

        return False

    def delete(self, key):
        index = self.hash_function(key)

        if key in self.table[index]:
            self.table[index].remove(key)
            return True

        return False


h = HashTable(10)

h.insert(25)
h.insert(35)
h.insert(45)
h.insert(12)

print(h.table)

print(h.search(35))

h.delete(35)

print(h.table)