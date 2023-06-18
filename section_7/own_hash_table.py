class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        addr = self._hash(key)
        if not self.data[addr]:
            self.data[addr] = []
        self.data[self._hash(key)].append([key, value])
        return self.data

    def get(self, key):
        current_bucket = self.data[self._hash(key)]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return "unidentified"


myHashTable = HashTable(2)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))
print("Data ",myHashTable.data)
