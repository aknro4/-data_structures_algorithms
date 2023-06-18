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

    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i]:
                # This solution only works whit large sizes
                keys_array.append(self.data[i][0][0])
                # This however works with all sizes or whit possible collision.
                # for j in range(len(self.data[i])):
                #     keys_array.append(self.data[i][j][0])
        return keys_array


myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))
print("Keys ",myHashTable.keys())
